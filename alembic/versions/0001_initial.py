from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "cars",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("model", sa.String(), nullable=False),
        sa.Column("available", sa.Boolean(), default=True),
    )
    op.create_table(
        "bookings",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("car_id", sa.Integer, nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("customer_name", sa.String(), nullable=False),
    )

def downgrade():
    op.drop_table("bookings")
    op.drop_table("cars")
