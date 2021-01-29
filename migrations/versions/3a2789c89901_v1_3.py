"""v1.3

Revision ID: 3a2789c89901
Revises: 851a00a0b178
Create Date: 2021-01-29 11:23:31.196350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a2789c89901'
down_revision = '851a00a0b178'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('courseholes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('course', 'courseholes')
    # ### end Alembic commands ###
