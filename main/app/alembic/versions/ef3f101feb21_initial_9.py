"""Initial 9

Revision ID: ef3f101feb21
Revises: de84556d9e2a
Create Date: 2021-11-14 06:45:24.012682

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'ef3f101feb21'
down_revision = 'de84556d9e2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('images', sa.Column('url_600', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.drop_column('images', 'url_600')
    # ### end Alembic commands ###
