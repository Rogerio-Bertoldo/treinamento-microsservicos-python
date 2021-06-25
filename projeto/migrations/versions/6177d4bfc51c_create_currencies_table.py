"""create currencies table

Revision ID: 6177d4bfc51c
Revises: 
Create Date: 2021-06-21 06:58:21.479937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6177d4bfc51c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currencies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('currencies')
    # ### end Alembic commands ###
