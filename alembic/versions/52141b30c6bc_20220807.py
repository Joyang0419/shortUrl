"""20220807

Revision ID: 52141b30c6bc
Revises: 
Create Date: 2022-08-07 00:19:27.584916

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '52141b30c6bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', mysql.BIGINT(display_width=20).with_variant(sa.Integer(), 'sqlite'), autoincrement=True, nullable=False, comment='ID'),
    sa.Column('account', mysql.VARCHAR(length=100), nullable=False, comment='user user'),
    sa.Column('password', mysql.VARCHAR(length=100), nullable=False, comment='user password'),
    sa.Column('create_time', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False, comment='建立時間'),
    sa.Column('update_time', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False, comment='修改時間'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account'),
    comment='帳號資訊'
    )
    op.create_table('short_url',
    sa.Column('id', mysql.BIGINT(display_width=20).with_variant(sa.Integer(), 'sqlite'), autoincrement=True, nullable=False, comment='ID'),
    sa.Column('user_id', mysql.BIGINT(display_width=20), nullable=False, comment='用戶資訊ID'),
    sa.Column('short_url', sa.String(length=2000), nullable=False, comment='短網址'),
    sa.Column('target_url', sa.String(length=2000), nullable=False, comment='長網址'),
    sa.Column('create_time', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False, comment='建立時間'),
    sa.Column('update_time', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False, comment='修改時間'),
    sa.PrimaryKeyConstraint('id'),
    comment='短網址表',
    sqlite_autoincrement=True
    )
    op.create_index(op.f('ix_short_url_user_id'), 'short_url', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_short_url_user_id'), table_name='short_url')
    op.drop_table('short_url')
    op.drop_table('account')
    # ### end Alembic commands ###
