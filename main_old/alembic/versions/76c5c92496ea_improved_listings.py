"""Improved Listings

Revision ID: 76c5c92496ea
Revises: 1038f05634e6
Create Date: 2021-11-08 21:34:17.068563

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '76c5c92496ea'
down_revision = '1038f05634e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image_tags',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('image_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['image_id'], ['images.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_image_tags_id'), 'image_tags', ['id'], unique=False)
    op.drop_column('images', 'updated_at')
    op.drop_column('listing_distances', 'updated_at')
    op.add_column('listings', sa.Column('ber_code', sa.String(length=10), nullable=True))
    op.add_column('listings', sa.Column('price', sa.Integer(), nullable=True))
    op.add_column('listings', sa.Column('rating_auto', sa.Integer(), nullable=True))
    op.add_column('listings', sa.Column('rating_user', sa.Integer(), nullable=True))
    op.add_column('listings', sa.Column('telegram_sent_at', sa.DateTime(), nullable=True))
    op.drop_column('listings', 'updated_at')
    op.drop_column('points', 'updated_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('points', sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('listings', sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('listings', 'telegram_sent_at')
    op.drop_column('listings', 'rating_user')
    op.drop_column('listings', 'rating_auto')
    op.drop_column('listings', 'price')
    op.drop_column('listings', 'ber_code')
    op.add_column('listing_distances', sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('images', sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_image_tags_id'), table_name='image_tags')
    op.drop_table('image_tags')
    # ### end Alembic commands ###
