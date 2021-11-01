"""distances 4

Revision ID: ae656d76b2f1
Revises: 94c2f18b742c
Create Date: 2021-11-01 00:00:44.703478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae656d76b2f1'
down_revision = '94c2f18b742c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('listing_distances',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('distance_km', sa.Float(), nullable=True),
    sa.Column('listing_id', sa.Integer(), nullable=True),
    sa.Column('point_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.ForeignKeyConstraint(['point_id'], ['points.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_listing_distances_id'), 'listing_distances', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_listing_distances_id'), table_name='listing_distances')
    op.drop_table('listing_distances')
    # ### end Alembic commands ###