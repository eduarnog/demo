"""add notes and user

Revision ID: d9b7547dbe2f
Revises: 
Create Date: 2023-04-26 16:02:30.505235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9b7547dbe2f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('password', sa.String(length=150), nullable=True),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('picture_url', sa.String(length=260), nullable=True),
    sa.Column('slug', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(length=10000), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('note')
    op.drop_table('user')
    # ### end Alembic commands ###
