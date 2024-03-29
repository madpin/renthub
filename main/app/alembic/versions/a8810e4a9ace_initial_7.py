"""Initial 7

Revision ID: a8810e4a9ace
Revises: 2be8e05a6a4f
Create Date: 2021-11-14 02:33:09.091191

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a8810e4a9ace'
down_revision = '2be8e05a6a4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('routes', sa.Column('walking_distance', sa.Integer(), nullable=True))
    op.add_column('routes', sa.Column('total_distance', sa.Integer(), nullable=True))
    op.add_column('routes', sa.Column('total_time', sa.Integer(), nullable=True))
    op.add_column('routes', sa.Column('public_transport_count', sa.Integer(), nullable=True))
    op.add_column('routes', sa.Column('interest_point_id', sa.Integer(), nullable=True))
    op.drop_index('ix_routes_address', table_name='routes')
    op.drop_index('ix_routes_chain_name', table_name='routes')
    op.drop_index('ix_routes_distance', table_name='routes')
    op.drop_index('ix_routes_latitude', table_name='routes')
    op.drop_index('ix_routes_longitude', table_name='routes')
    op.drop_index('ix_routes_name', table_name='routes')
    op.drop_index('ix_routes_website', table_name='routes')
    op.drop_index('ix_routes_website_domain', table_name='routes')
    op.create_index(op.f('ix_routes_interest_point_id'), 'routes', ['interest_point_id'], unique=False)
    op.create_index(op.f('ix_routes_public_transport_count'), 'routes', ['public_transport_count'], unique=False)
    op.create_index(op.f('ix_routes_total_distance'), 'routes', ['total_distance'], unique=False)
    op.create_index(op.f('ix_routes_total_time'), 'routes', ['total_time'], unique=False)
    op.create_index(op.f('ix_routes_walking_distance'), 'routes', ['walking_distance'], unique=False)
    op.create_foreign_key(None, 'routes', 'interest_points', ['interest_point_id'], ['id'])
    op.drop_column('routes', 'address')
    op.drop_column('routes', 'name')
    op.drop_column('routes', 'latitude')
    op.drop_column('routes', 'longitude')
    op.drop_column('routes', 'distance')
    op.drop_column('routes', 'chain_name')
    op.drop_column('routes', 'website')
    op.drop_column('routes', 'website_domain')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('routes', sa.Column('website_domain', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('routes', sa.Column('website', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('routes', sa.Column('chain_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('routes', sa.Column('distance', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('routes', sa.Column('longitude', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('routes', sa.Column('latitude', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('routes', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('routes', sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'routes', type_='foreignkey')
    op.drop_index(op.f('ix_routes_walking_distance'), table_name='routes')
    op.drop_index(op.f('ix_routes_total_time'), table_name='routes')
    op.drop_index(op.f('ix_routes_total_distance'), table_name='routes')
    op.drop_index(op.f('ix_routes_public_transport_count'), table_name='routes')
    op.drop_index(op.f('ix_routes_interest_point_id'), table_name='routes')
    op.create_index('ix_routes_website_domain', 'routes', ['website_domain'], unique=False)
    op.create_index('ix_routes_website', 'routes', ['website'], unique=False)
    op.create_index('ix_routes_name', 'routes', ['name'], unique=False)
    op.create_index('ix_routes_longitude', 'routes', ['longitude'], unique=False)
    op.create_index('ix_routes_latitude', 'routes', ['latitude'], unique=False)
    op.create_index('ix_routes_distance', 'routes', ['distance'], unique=False)
    op.create_index('ix_routes_chain_name', 'routes', ['chain_name'], unique=False)
    op.create_index('ix_routes_address', 'routes', ['address'], unique=False)
    op.drop_column('routes', 'interest_point_id')
    op.drop_column('routes', 'public_transport_count')
    op.drop_column('routes', 'total_time')
    op.drop_column('routes', 'total_distance')
    op.drop_column('routes', 'walking_distance')
    # ### end Alembic commands ###
