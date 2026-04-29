# repository/fare_repository.py

from sqlalchemy.orm import Session
from database.model import FareRecord


class FareRepository:
    """
    Repository layer for FareRecord entity.

    This class provides methods to interact with the database for
    FareRecord operations. It abstracts raw database queries and ensures
    separation between business logic (service layer) and persistence logic.

    Notes:
        - This layer does NOT handle transactions (commit/rollback).
        - Transaction management must be handled in the service layer.
        - All methods expect an active SQLAlchemy Session.
    """

    @staticmethod
    def add(db: Session, record: FareRecord) -> FareRecord:
        """
        Add a new fare record to the database session.

        This method stages the given FareRecord object for insertion
        into the database. It does NOT commit the transaction. The
        caller (typically the service layer) is responsible for
        committing or rolling back the transaction.

        Args:
            db (Session): Active SQLAlchemy database session.
            record (FareRecord): FareRecord instance containing
                                 ride and fare details.

        Returns:
            FareRecord: The same FareRecord instance added to the session.

        Notes:
            - This method does not call `commit()` or `rollback()`.
            - Use `db.commit()` in the service layer to persist changes.
            - Use `db.refresh(record)` after commit to get updated values
              (e.g., auto-generated ID).

        Raises:
            sqlalchemy.exc.SQLAlchemyError: If the record cannot be added
                                           to the session (raised during commit).
        """
        db.add(record)
        return record

    @staticmethod
    def get_all(db: Session) -> list[FareRecord]:
        """
        Retrieve all fare records from the database.

        This method fetches all records from the FareRecord table,
        ordered by their ID in descending order (latest records first).

        Args:
            db (Session): Active SQLAlchemy database session.

        Returns:
            list[FareRecord]: List of FareRecord objects.

        Notes:
            - This method performs a read-only operation.
            - No transaction commit is required.
            - The result is fully loaded into memory.

        Raises:
            sqlalchemy.exc.SQLAlchemyError: If the query execution fails.
        """
        return db.query(FareRecord).order_by(FareRecord.id.desc()).all()