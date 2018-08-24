"""empty message

Revision ID: 5f6f6fae7453
Revises: 
Create Date: 2018-08-24 19:11:02.252773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f6f6fae7453'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('home_team_name', sa.String(length=45), nullable=True),
    sa.Column('home_team_city_abbr', sa.String(length=10), nullable=True),
    sa.Column('home_team_score', sa.Integer(), nullable=True),
    sa.Column('away_team_name', sa.String(length=45), nullable=True),
    sa.Column('away_team_city_abbr', sa.String(length=10), nullable=True),
    sa.Column('away_team_score', sa.Integer(), nullable=True),
    sa.Column('day_of_week', sa.String(length=3), nullable=True),
    sa.Column('time', sa.String(length=5), nullable=True),
    sa.Column('game_date', sa.DateTime(), nullable=True),
    sa.Column('quarter', sa.String(length=3), nullable=True),
    sa.Column('week', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('game_id')
    )
    op.create_table('leagues',
    sa.Column('league_id', sa.Integer(), nullable=False),
    sa.Column('league_name', sa.String(length=50), nullable=False),
    sa.Column('league_description', sa.String(length=500), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('league_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.String(length=45), nullable=False),
    sa.Column('full_name', sa.String(length=45), nullable=True),
    sa.Column('email', sa.String(length=45), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('picture_url', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('admin_messages',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=45), nullable=True),
    sa.Column('message_text', sa.String(length=500), nullable=False),
    sa.Column('show_message', sa.Boolean(), nullable=True),
    sa.Column('message_type', sa.String(length=25), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('message_id')
    )
    op.create_table('player_teams',
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('league_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=45), nullable=True),
    sa.Column('team_name', sa.String(length=105), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('has_paid', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['league_id'], ['leagues.league_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('team_id'),
    sa.UniqueConstraint('team_name')
    )
    op.create_table('picks',
    sa.Column('pick_id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('week_num', sa.Integer(), nullable=False),
    sa.Column('nfl_team_name', sa.String(length=30), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.game_id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['player_teams.team_id'], ),
    sa.PrimaryKeyConstraint('pick_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('picks')
    op.drop_table('player_teams')
    op.drop_table('admin_messages')
    op.drop_table('users')
    op.drop_table('leagues')
    op.drop_table('games')
    # ### end Alembic commands ###
