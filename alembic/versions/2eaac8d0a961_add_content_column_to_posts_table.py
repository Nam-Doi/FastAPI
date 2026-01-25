"""add content column to posts table

Revision ID: 2eaac8d0a961
Revises: 8b505dbc38e7
Create Date: 2026-01-25 10:52:55.008429

"""
from time import timezone
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2eaac8d0a961'
down_revision: Union[str, Sequence[str], None] = '8b505dbc38e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass
