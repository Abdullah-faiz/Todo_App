"""empty message

Revision ID: b6238bb5e462
Revises: e13d27dbf5d7
Create Date: 2022-11-29 23:27:44.598700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6238bb5e462'
down_revision = 'e13d27dbf5d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_password_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_password_key', 'user', ['password'])
    # ### end Alembic commands ###
