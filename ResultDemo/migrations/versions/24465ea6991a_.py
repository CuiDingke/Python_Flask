"""empty message

Revision ID: 24465ea6991a
Revises: 
Create Date: 2021-10-07 16:44:47.675607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24465ea6991a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('password', sa.String(length=15), nullable=False),
    sa.Column('udatetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###