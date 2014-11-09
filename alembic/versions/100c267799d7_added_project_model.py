"""Added project model

Revision ID: 100c267799d7
Revises: None
Create Date: 2014-11-09 18:31:46.035029

"""

# revision identifiers, used by Alembic.
revision = '100c267799d7'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'User', ['user_name'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'User')
    ### end Alembic commands ###
