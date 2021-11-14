"""Initial 5

Revision ID: 0101e666f4e9
Revises: 6c98e82ae2b5
Create Date: 2021-11-14 01:40:19.792380

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '0101e666f4e9'
down_revision = '6c98e82ae2b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interest_points',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('address', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('distance', sa.Integer(), nullable=False),
    sa.Column('website', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('website_domain', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('chain_name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('listing_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_interest_points_address'), 'interest_points', ['address'], unique=False)
    op.create_index(op.f('ix_interest_points_chain_name'), 'interest_points', ['chain_name'], unique=False)
    op.create_index(op.f('ix_interest_points_created_at'), 'interest_points', ['created_at'], unique=False)
    op.create_index(op.f('ix_interest_points_distance'), 'interest_points', ['distance'], unique=False)
    op.create_index(op.f('ix_interest_points_id'), 'interest_points', ['id'], unique=False)
    op.create_index(op.f('ix_interest_points_latitude'), 'interest_points', ['latitude'], unique=False)
    op.create_index(op.f('ix_interest_points_listing_id'), 'interest_points', ['listing_id'], unique=False)
    op.create_index(op.f('ix_interest_points_longitude'), 'interest_points', ['longitude'], unique=False)
    op.create_index(op.f('ix_interest_points_name'), 'interest_points', ['name'], unique=False)
    op.create_index(op.f('ix_interest_points_updated_at'), 'interest_points', ['updated_at'], unique=False)
    op.create_index(op.f('ix_interest_points_website'), 'interest_points', ['website'], unique=False)
    op.create_index(op.f('ix_interest_points_website_domain'), 'interest_points', ['website_domain'], unique=False)
    op.create_table('places_nearby',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('address', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('distance', sa.Integer(), nullable=False),
    sa.Column('website', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('website_domain', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('chain_name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('listing_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_places_nearby_address'), 'places_nearby', ['address'], unique=False)
    op.create_index(op.f('ix_places_nearby_chain_name'), 'places_nearby', ['chain_name'], unique=False)
    op.create_index(op.f('ix_places_nearby_created_at'), 'places_nearby', ['created_at'], unique=False)
    op.create_index(op.f('ix_places_nearby_distance'), 'places_nearby', ['distance'], unique=False)
    op.create_index(op.f('ix_places_nearby_id'), 'places_nearby', ['id'], unique=False)
    op.create_index(op.f('ix_places_nearby_latitude'), 'places_nearby', ['latitude'], unique=False)
    op.create_index(op.f('ix_places_nearby_listing_id'), 'places_nearby', ['listing_id'], unique=False)
    op.create_index(op.f('ix_places_nearby_longitude'), 'places_nearby', ['longitude'], unique=False)
    op.create_index(op.f('ix_places_nearby_name'), 'places_nearby', ['name'], unique=False)
    op.create_index(op.f('ix_places_nearby_updated_at'), 'places_nearby', ['updated_at'], unique=False)
    op.create_index(op.f('ix_places_nearby_website'), 'places_nearby', ['website'], unique=False)
    op.create_index(op.f('ix_places_nearby_website_domain'), 'places_nearby', ['website_domain'], unique=False)
    op.create_table('routes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('address', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('distance', sa.Integer(), nullable=False),
    sa.Column('website', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('website_domain', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('chain_name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('listing_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_routes_address'), 'routes', ['address'], unique=False)
    op.create_index(op.f('ix_routes_chain_name'), 'routes', ['chain_name'], unique=False)
    op.create_index(op.f('ix_routes_created_at'), 'routes', ['created_at'], unique=False)
    op.create_index(op.f('ix_routes_distance'), 'routes', ['distance'], unique=False)
    op.create_index(op.f('ix_routes_id'), 'routes', ['id'], unique=False)
    op.create_index(op.f('ix_routes_latitude'), 'routes', ['latitude'], unique=False)
    op.create_index(op.f('ix_routes_listing_id'), 'routes', ['listing_id'], unique=False)
    op.create_index(op.f('ix_routes_longitude'), 'routes', ['longitude'], unique=False)
    op.create_index(op.f('ix_routes_name'), 'routes', ['name'], unique=False)
    op.create_index(op.f('ix_routes_updated_at'), 'routes', ['updated_at'], unique=False)
    op.create_index(op.f('ix_routes_website'), 'routes', ['website'], unique=False)
    op.create_index(op.f('ix_routes_website_domain'), 'routes', ['website_domain'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_routes_website_domain'), table_name='routes')
    op.drop_index(op.f('ix_routes_website'), table_name='routes')
    op.drop_index(op.f('ix_routes_updated_at'), table_name='routes')
    op.drop_index(op.f('ix_routes_name'), table_name='routes')
    op.drop_index(op.f('ix_routes_longitude'), table_name='routes')
    op.drop_index(op.f('ix_routes_listing_id'), table_name='routes')
    op.drop_index(op.f('ix_routes_latitude'), table_name='routes')
    op.drop_index(op.f('ix_routes_id'), table_name='routes')
    op.drop_index(op.f('ix_routes_distance'), table_name='routes')
    op.drop_index(op.f('ix_routes_created_at'), table_name='routes')
    op.drop_index(op.f('ix_routes_chain_name'), table_name='routes')
    op.drop_index(op.f('ix_routes_address'), table_name='routes')
    op.drop_table('routes')
    op.drop_index(op.f('ix_places_nearby_website_domain'), table_name='places_nearby')
    op.drop_index(op.f('ix_places_nearby_website'), table_name='places_nearby')
    op.drop_index(op.f('ix_places_nearby_updated_at'), table_name='places_nearby')
    op.drop_index(op.f('ix_places_nearby_name'), table_name='places_nearby')
    op.drop_index(op.f('ix_places_nearby_longitude'), table_name='places_nearby')
    op.drop_index(op.f('ix_places_nearby_listing_id'), table_name='places_nearby')
    op.drop_index(op.f('ix_places_nearby_latitude'), table_name='places_nearby')
    op.drop_index(op.f('ix_places_nearby_id'), table_name='places_nearby')
    op.drop_index(op.f('ix_places_nearby_distance'), table_name='places_nearby')
    op.drop_index(op.f('ix_places_nearby_created_at'), table_name='places_nearby')
    op.drop_index(op.f('ix_places_nearby_chain_name'), table_name='places_nearby')
    op.drop_index(op.f('ix_places_nearby_address'), table_name='places_nearby')
    op.drop_table('places_nearby')
    op.drop_index(op.f('ix_interest_points_website_domain'), table_name='interest_points')
    op.drop_index(op.f('ix_interest_points_website'), table_name='interest_points')
    op.drop_index(op.f('ix_interest_points_updated_at'), table_name='interest_points')
    op.drop_index(op.f('ix_interest_points_name'), table_name='interest_points')
    op.drop_index(op.f('ix_interest_points_longitude'), table_name='interest_points')
    op.drop_index(op.f('ix_interest_points_listing_id'), table_name='interest_points')
    op.drop_index(op.f('ix_interest_points_latitude'), table_name='interest_points')
    op.drop_index(op.f('ix_interest_points_id'), table_name='interest_points')
    op.drop_index(op.f('ix_interest_points_distance'), table_name='interest_points')
    op.drop_index(op.f('ix_interest_points_created_at'), table_name='interest_points')
    op.drop_index(op.f('ix_interest_points_chain_name'), table_name='interest_points')
    op.drop_index(op.f('ix_interest_points_address'), table_name='interest_points')
    op.drop_table('interest_points')
    # ### end Alembic commands ###