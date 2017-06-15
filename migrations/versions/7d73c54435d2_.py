"""empty message

Revision ID: 7d73c54435d2
Revises: 
Create Date: 2017-06-01 19:37:51.412250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d73c54435d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('second_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('row', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('second_table')
    # ### end Alembic commands ###