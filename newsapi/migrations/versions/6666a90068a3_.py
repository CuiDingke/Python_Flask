"""empty message

Revision ID: 6666a90068a3
Revises: 4eb54e4e1063
Create Date: 2021-10-22 15:54:51.020204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6666a90068a3'
down_revision = '4eb54e4e1063'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('icon', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
