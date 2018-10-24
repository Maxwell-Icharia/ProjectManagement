"""Added column project name

Revision ID: 6487fba54716
Revises: e87727ca0d50
Create Date: 2018-10-18 09:47:04.354347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6487fba54716'
down_revision = 'e87727ca0d50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Register', sa.Column('project_name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Register', 'project_name')
    # ### end Alembic commands ###