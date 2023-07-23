"""create items table

Revision ID: 80a8b7beeefc
Revises: 
Create Date: 2023-07-23 11:32:57.527657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80a8b7beeefc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('items', sa.Column('itemId', sa.Integer(), primary_key=True),
                    sa.Column('itemName', sa.String(), nullable=False),
                    sa.Column('description', sa.String(), nullable=False),
                    sa.Column('price', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_table('items')
