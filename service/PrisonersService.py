import tempfile


import os
import openpyxl
import datetime
from fastapi import UploadFile
from dao.repository.PrisonersRepository import *

CHUNK_SIZE = 1024 * 1024  # 1 MB chunks

class PrisonersService:
    def __init__(self, db: Session):
        self.db = db
        self.buffer = None
        self.filename = None
        self.expected_size = None
        self.received_size = 0
        self.prisonersRepo = PrisonersRepository(db)

    @staticmethod
    def is_header_row(row):
        """Detect header rows by common Azerbaijani column names."""
        text = " ".join([str(c).lower() for c in row if c])
        keywords = ["adı", "soyadı", "ata", "fin", "doğum", "ş.v", "modul", "müəssisə"]

        return any(k in text for k in keywords)

    async def save_real_excel_stream(self, file: UploadFile):
        # Create temp file on disk
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
        tmp_name = tmp.name

        # Write chunks
        while chunk := await file.read(CHUNK_SIZE):
            tmp.write(chunk)

        tmp.close()

        prisoners_batch = []

        try:
            workbook = openpyxl.load_workbook(tmp_name, read_only=True, data_only=True)

            for sheet_name in workbook.sheetnames:
                sheet = workbook[sheet_name]

                for row in sheet.iter_rows(values_only=True):

                    # 1. Skip empty rows
                    if not row or not row[0]:
                        continue

                    # 2. Skip header rows
                    if self.is_header_row(row):
                        continue

                    # 3. Extract name parts
                    adi = row[0] if len(row) > 0 else None
                    soyadi = row[1] if len(row) > 1 else None
                    ata_adi = row[2] if len(row) > 2 else None

                    full_name = " ".join([str(x) for x in [adi, soyadi, ata_adi] if x])

                    # 4. Helper conversion functions
                    def to_int(value):
                        try:
                            return int(value)
                        except:
                            return None

                    def to_date(value):
                        if isinstance(value, (datetime.datetime, datetime.date)):
                            return value
                        return None

                    # 5. Mapping to Prisoner fields
                    prisoner = {
                        "full_name": full_name,

                        "organization_id": to_int(row[3]) if len(row) > 3 else None,
                        "module_id": to_int(row[4]) if len(row) > 4 else None,
                        "sub_module_id": to_int(row[5]) if len(row) > 5 else None,
                        "division": to_int(row[6]) if len(row) > 6 else None,
                        "personal_number": to_int(row[7]) if len(row) > 7 else None,

                        "last_meet_date": to_date(row[8]) if len(row) > 8 else None,
                        "photo_id": to_int(row[9]) if len(row) > 9 else None,

                        "short_term_permit": to_int(row[10]) if len(row) > 10 else None,
                        "long_term_permit": to_int(row[11]) if len(row) > 11 else None,

                        "visit_item": to_int(row[12]) if len(row) > 12 else None,
                        "parcel": to_int(row[13]) if len(row) > 13 else None,

                        "article": row[14] if len(row) > 14 else None,
                        "pin": row[15] if len(row) > 15 else None,

                        "serial_type_id": to_int(row[16]) if len(row) > 16 else None,
                        "serial_number": row[17] if len(row) > 17 else None,

                        "birth_date": to_date(row[18]) if len(row) > 18 else None,
                        "start_date": to_date(row[19]) if len(row) > 19 else None,
                        "end_date": to_date(row[20]) if len(row) > 20 else None,

                        "deleted": False,
                    }

                    prisoners_batch.append(prisoner)

                    # 6. Save in chunks of 500
                    if len(prisoners_batch) >= 500:
                        self.prisonersRepo.save_all_prisoners(prisoners_batch)
                        prisoners_batch = []

            # Save remaining rows
            if prisoners_batch:
                self.prisonersRepo.save_all_prisoners(prisoners_batch)

            workbook.close()

        finally:
            try:
                os.remove(tmp_name)
            except Exception as e:
                print("Cleanup error:", e)

        return {"status": "ok"}










