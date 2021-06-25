"""create quotations table

Revision ID: 178730f248a3
Revises: 6177d4bfc51c
Create Date: 2021-06-21 07:05:23.820273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '178730f248a3'
down_revision = '6177d4bfc51c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quotations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_currency_id', sa.Integer(), nullable=True),
    sa.Column('from_currency_value', sa.Float(), nullable=True),
    sa.Column('to_currency_id', sa.Integer(), nullable=True),
    sa.Column('to_currency_value', sa.Float(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['from_currency_id'], ['currencies.id'], ),
    sa.ForeignKeyConstraint(['to_currency_id'], ['currencies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quotations')
    # ### end Alembic commands ###