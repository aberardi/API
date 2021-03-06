"""empty message

Revision ID: 8fb3a0bd4a39
Revises: 9d882d87efbd
Create Date: 2018-08-24 23:40:21.729138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fb3a0bd4a39'
down_revision = '9d882d87efbd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('stadium_id', sa.Integer(), nullable=True))
    op.drop_constraint('games_site_id_fkey', 'games', type_='foreignkey')
    op.create_foreign_key(None, 'games', 'stadiums', ['stadium_id'], ['stadium_id'])
    op.drop_column('games', 'site_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('site_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'games', type_='foreignkey')
    op.create_foreign_key('games_site_id_fkey', 'games', 'stadiums', ['site_id'], ['stadium_id'])
    op.drop_column('games', 'stadium_id')
    # ### end Alembic commands ###
