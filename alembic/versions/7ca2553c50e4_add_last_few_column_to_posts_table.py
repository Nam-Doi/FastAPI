"""add last few column to posts table

Revision ID: 7ca2553c50e4
Revises: dd8fe75bdbeb
Create Date: 2026-01-25 11:26:38.981646

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ca2553c50e4'
down_revision: Union[str, Sequence[str], None] = 'dd8fe75bdbeb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    #add column chi add 1 cot
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE')
        )
    op.add_column('posts',
                  sa.Column('created_at',sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'),nullable=False)
                              )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
