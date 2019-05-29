"""empty message

Revision ID: 51e0f450466c
Revises: 
Create Date: 2019-05-28 20:03:14.732117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51e0f450466c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('amostra',
    sa.Column('idmodelo', sa.Integer(), nullable=False),
    sa.Column('idamostra', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tpamostra', sa.String(), nullable=False),
    sa.Column('dsobservacoes', sa.String(), nullable=True),
    sa.Column('dtcoletaamostra', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('idmodelo', 'idamostra')
    )
    op.create_table('amostra_calibracao',
    sa.Column('idmodelo', sa.Integer(), nullable=False),
    sa.Column('idamostra', sa.Integer(), nullable=False),
    sa.Column('idcalibracao', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('idmodelo', 'idamostra', 'idcalibracao')
    )
    op.create_table('calibracao',
    sa.Column('idmodelo', sa.Integer(), nullable=False),
    sa.Column('idcalibracao', sa.Integer(), nullable=False),
    sa.Column('inativo', sa.String(), nullable=True),
    sa.Column('dtcalibracao', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('idmodelo', 'idcalibracao')
    )
    op.create_table('matrizX',
    sa.Column('idmodelo', sa.Integer(), nullable=False),
    sa.Column('idamostra', sa.Integer(), nullable=False),
    sa.Column('nrsequencia', sa.Integer(), nullable=False),
    sa.Column('nrposicaolinha', sa.Integer(), nullable=False),
    sa.Column('nrposicaocoluna', sa.Integer(), nullable=False),
    sa.Column('vllinhacoluna', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('idmodelo', 'idamostra', 'nrsequencia')
    )
    op.create_table('matrizY',
    sa.Column('idmodelo', sa.Integer(), nullable=False),
    sa.Column('idamostra', sa.Integer(), nullable=False),
    sa.Column('idparametroref', sa.Integer(), nullable=False),
    sa.Column('idcalibracao', sa.Integer(), nullable=False),
    sa.Column('vlresultado', sa.Numeric(), nullable=False),
    sa.Column('vlreferencia', sa.Numeric(), nullable=False),
    sa.Column('dtpredicao', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('idmodelo', 'idamostra', 'idparametroref')
    )
    op.create_table('modelo',
    sa.Column('idmodelo', sa.Integer(), nullable=False),
    sa.Column('nmmodelo', sa.String(), nullable=False),
    sa.Column('nmmetodoreferencia', sa.String(), nullable=False),
    sa.Column('tpinstrumento', sa.String(), nullable=False),
    sa.Column('dsmodelo', sa.String(), nullable=True),
    sa.Column('dtcriacao', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('idmodelo'),
    sa.UniqueConstraint('nmmodelo')
    )
    op.create_table('parametro',
    sa.Column('idmodelo', sa.Integer(), nullable=False),
    sa.Column('idparametroref', sa.Integer(), nullable=False),
    sa.Column('nmparametroref', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('idmodelo', 'idparametroref')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parametro')
    op.drop_table('modelo')
    op.drop_table('matrizY')
    op.drop_table('matrizX')
    op.drop_table('calibracao')
    op.drop_table('amostra_calibracao')
    op.drop_table('amostra')
    # ### end Alembic commands ###
