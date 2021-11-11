"""Initial

Revision ID: a269901d7390
Revises: 
Create Date: 2021-11-10 01:48:12.091332

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'a269901d7390'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facilities',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('category', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('notes', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_facilities_category'), 'facilities', ['category'], unique=False)
    op.create_index(op.f('ix_facilities_created_at'), 'facilities', ['created_at'], unique=False)
    op.create_index(op.f('ix_facilities_id'), 'facilities', ['id'], unique=False)
    op.create_index(op.f('ix_facilities_name'), 'facilities', ['name'], unique=False)
    op.create_index(op.f('ix_facilities_notes'), 'facilities', ['notes'], unique=False)
    op.create_index(op.f('ix_facilities_updated_at'), 'facilities', ['updated_at'], unique=False)
    op.create_table('increment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_increment_id'), 'increment', ['id'], unique=False)
    op.create_table('listings',
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('source', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('address', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('short_postal_code', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('postal_code', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('ber_code', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('rating_auto', sa.Integer(), nullable=True),
    sa.Column('rating_user', sa.Integer(), nullable=True),
    sa.Column('telegram_sent_at', sa.DateTime(), nullable=True),
    sa.Column('images_count', sa.Integer(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('notes', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_listings_address'), 'listings', ['address'], unique=False)
    op.create_index(op.f('ix_listings_ber_code'), 'listings', ['ber_code'], unique=False)
    op.create_index(op.f('ix_listings_created_at'), 'listings', ['created_at'], unique=False)
    op.create_index(op.f('ix_listings_id'), 'listings', ['id'], unique=False)
    op.create_index(op.f('ix_listings_images_count'), 'listings', ['images_count'], unique=False)
    op.create_index(op.f('ix_listings_is_active'), 'listings', ['is_active'], unique=False)
    op.create_index(op.f('ix_listings_latitude'), 'listings', ['latitude'], unique=False)
    op.create_index(op.f('ix_listings_longitude'), 'listings', ['longitude'], unique=False)
    op.create_index(op.f('ix_listings_notes'), 'listings', ['notes'], unique=False)
    op.create_index(op.f('ix_listings_postal_code'), 'listings', ['postal_code'], unique=False)
    op.create_index(op.f('ix_listings_price'), 'listings', ['price'], unique=False)
    op.create_index(op.f('ix_listings_rating_auto'), 'listings', ['rating_auto'], unique=False)
    op.create_index(op.f('ix_listings_rating_user'), 'listings', ['rating_user'], unique=False)
    op.create_index(op.f('ix_listings_short_postal_code'), 'listings', ['short_postal_code'], unique=False)
    op.create_index(op.f('ix_listings_source'), 'listings', ['source'], unique=False)
    op.create_index(op.f('ix_listings_telegram_sent_at'), 'listings', ['telegram_sent_at'], unique=False)
    op.create_index(op.f('ix_listings_title'), 'listings', ['title'], unique=False)
    op.create_index(op.f('ix_listings_updated_at'), 'listings', ['updated_at'], unique=False)
    op.create_index(op.f('ix_listings_url'), 'listings', ['url'], unique=False)
    op.create_table('song',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('artist', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_song_artist'), 'song', ['artist'], unique=False)
    op.create_index(op.f('ix_song_created_at'), 'song', ['created_at'], unique=False)
    op.create_index(op.f('ix_song_id'), 'song', ['id'], unique=False)
    op.create_index(op.f('ix_song_name'), 'song', ['name'], unique=False)
    op.create_index(op.f('ix_song_updated_at'), 'song', ['updated_at'], unique=False)
    op.create_index(op.f('ix_song_year'), 'song', ['year'], unique=False)
    op.create_table('images',
    sa.Column('url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('size_x', sa.Float(), nullable=False),
    sa.Column('size_y', sa.Float(), nullable=False),
    sa.Column('listing_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_images_created_at'), 'images', ['created_at'], unique=False)
    op.create_index(op.f('ix_images_id'), 'images', ['id'], unique=False)
    op.create_index(op.f('ix_images_listing_id'), 'images', ['listing_id'], unique=False)
    op.create_index(op.f('ix_images_size_x'), 'images', ['size_x'], unique=False)
    op.create_index(op.f('ix_images_size_y'), 'images', ['size_y'], unique=False)
    op.create_index(op.f('ix_images_updated_at'), 'images', ['updated_at'], unique=False)
    op.create_index(op.f('ix_images_url'), 'images', ['url'], unique=False)
    op.create_table('listingfacilitylink',
    sa.Column('listing_id', sa.Integer(), nullable=True),
    sa.Column('facility_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['facility_id'], ['facilities.id'], ),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.PrimaryKeyConstraint('listing_id', 'facility_id')
    )
    op.create_index(op.f('ix_listingfacilitylink_facility_id'), 'listingfacilitylink', ['facility_id'], unique=False)
    op.create_index(op.f('ix_listingfacilitylink_listing_id'), 'listingfacilitylink', ['listing_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_listingfacilitylink_listing_id'), table_name='listingfacilitylink')
    op.drop_index(op.f('ix_listingfacilitylink_facility_id'), table_name='listingfacilitylink')
    op.drop_table('listingfacilitylink')
    op.drop_index(op.f('ix_images_url'), table_name='images')
    op.drop_index(op.f('ix_images_updated_at'), table_name='images')
    op.drop_index(op.f('ix_images_size_y'), table_name='images')
    op.drop_index(op.f('ix_images_size_x'), table_name='images')
    op.drop_index(op.f('ix_images_listing_id'), table_name='images')
    op.drop_index(op.f('ix_images_id'), table_name='images')
    op.drop_index(op.f('ix_images_created_at'), table_name='images')
    op.drop_table('images')
    op.drop_index(op.f('ix_song_year'), table_name='song')
    op.drop_index(op.f('ix_song_updated_at'), table_name='song')
    op.drop_index(op.f('ix_song_name'), table_name='song')
    op.drop_index(op.f('ix_song_id'), table_name='song')
    op.drop_index(op.f('ix_song_created_at'), table_name='song')
    op.drop_index(op.f('ix_song_artist'), table_name='song')
    op.drop_table('song')
    op.drop_index(op.f('ix_listings_url'), table_name='listings')
    op.drop_index(op.f('ix_listings_updated_at'), table_name='listings')
    op.drop_index(op.f('ix_listings_title'), table_name='listings')
    op.drop_index(op.f('ix_listings_telegram_sent_at'), table_name='listings')
    op.drop_index(op.f('ix_listings_source'), table_name='listings')
    op.drop_index(op.f('ix_listings_short_postal_code'), table_name='listings')
    op.drop_index(op.f('ix_listings_rating_user'), table_name='listings')
    op.drop_index(op.f('ix_listings_rating_auto'), table_name='listings')
    op.drop_index(op.f('ix_listings_price'), table_name='listings')
    op.drop_index(op.f('ix_listings_postal_code'), table_name='listings')
    op.drop_index(op.f('ix_listings_notes'), table_name='listings')
    op.drop_index(op.f('ix_listings_longitude'), table_name='listings')
    op.drop_index(op.f('ix_listings_latitude'), table_name='listings')
    op.drop_index(op.f('ix_listings_is_active'), table_name='listings')
    op.drop_index(op.f('ix_listings_images_count'), table_name='listings')
    op.drop_index(op.f('ix_listings_id'), table_name='listings')
    op.drop_index(op.f('ix_listings_created_at'), table_name='listings')
    op.drop_index(op.f('ix_listings_ber_code'), table_name='listings')
    op.drop_index(op.f('ix_listings_address'), table_name='listings')
    op.drop_table('listings')
    op.drop_index(op.f('ix_increment_id'), table_name='increment')
    op.drop_table('increment')
    op.drop_index(op.f('ix_facilities_updated_at'), table_name='facilities')
    op.drop_index(op.f('ix_facilities_notes'), table_name='facilities')
    op.drop_index(op.f('ix_facilities_name'), table_name='facilities')
    op.drop_index(op.f('ix_facilities_id'), table_name='facilities')
    op.drop_index(op.f('ix_facilities_created_at'), table_name='facilities')
    op.drop_index(op.f('ix_facilities_category'), table_name='facilities')
    op.drop_table('facilities')
    # ### end Alembic commands ###