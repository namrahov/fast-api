"""add nurlan column on users table

Revision ID: 0dcc169af245
Revises: 
Create Date: 2026-02-02 12:29:04.048826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0dcc169af245'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.add_column('users', sa.Column('nurlan', sa.String(length=255), nullable=True))

def downgrade() -> None:
    """Downgrade schema."""
    pass
