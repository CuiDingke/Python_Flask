"""empty message

Revision ID: b4f0f613e808
Revises: 
Create Date: 2021-10-11 14:49:31.315031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4f0f613e808'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('base_model',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=True),
    sa.Column('type_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('base_model')
    # ### end Alembic commands ###
