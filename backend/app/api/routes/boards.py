# import uuid
from typing import Any

from fastapi import APIRouter, status
from app.api.deps import SessionDep

from app.models import Board, BoardCreate, BoardPublic
# from app import crud

router = APIRouter()


@router.post("/")
def create_board(
    *,
    session: SessionDep,
    # board_in: BoardCreate
    board_in: Board
    ) -> Any:
    """
    Create new board.
    """
    db_board = Board.model_validate(board_in)
    # db_board = BoardCreate.model_validation(board_in)

    session.add(db_board)
    session.commit()
    session.refresh(db_board)

    return db_board

@router.get("/")
def get_boards() -> Any:
    """
    Get boards
    """

    # Add in limit and stuff

