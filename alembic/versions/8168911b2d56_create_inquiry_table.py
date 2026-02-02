"""create inquiry table

Revision ID: 8168911b2d56
Revises: 0dcc169af245
Create Date: 2026-02-02 15:43:53.555036

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8168911b2d56'
down_revision: Union[str, Sequence[str], None] = '0dcc169af245'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('inquiry',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_inquiry_id'), 'inquiry', ['id'], unique=False)



def downgrade() -> None:
    """Downgrade schema."""
    pass
