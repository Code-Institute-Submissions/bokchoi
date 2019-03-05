"""empty message

Revision ID: d1a7f3420bfa
Revises: 59c7659991f9
Create Date: 2019-02-19 13:20:53.896521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1a7f3420bfa'
down_revision = '59c7659991f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_likes',
    sa.Column('liker_id', sa.Integer(), nullable=True),
    sa.Column('liked_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['liked_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['liker_id'], ['user.id'], )
    )
    op.drop_table('user_likes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_likes',
    sa.Column('liker_id', sa.INTEGER(), nullable=True),
    sa.Column('liked_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['liked_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['liker_id'], ['user.id'], )
    )
    op.drop_table('post_likes')
    # ### end Alembic commands ###
