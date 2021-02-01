"""v1.3.1

Revision ID: a0c050c9e8f8
Revises: 3a2789c89901
Create Date: 2021-01-30 13:31:41.999340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0c050c9e8f8'
down_revision = '3a2789c89901'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('courselocation', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('course', 'courselocation')
    # ### end Alembic commands ###