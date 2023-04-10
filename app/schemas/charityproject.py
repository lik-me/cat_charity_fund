from typing import Optional
from pydantic import BaseModel, Field, PositiveInt, validator
from datetime import datetime


class CharityprojectBase(BaseModel):

    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1)
    full_amount: Optional[PositiveInt] = Field(None)
    invested_amount: Optional[PositiveInt] = Field(None)

    @validator('full_amount', pre=True)
    def full_amount_not_null(cls, value):
        # print(value)
        if value == '':
            raise ValueError('Сумма пожертвования не может быть пустой!')
        elif value < 0:
            raise ValueError('Сумма пожертвования не может быть меньше 0!')
        elif value == 0:
            raise ValueError('Сумма пожертвования не может быть равна 0!')
        elif isinstance(value, int) is False:
            raise ValueError('Сумма пожертвования должна быть целым числом!')
        return value

    @validator('name', pre=True)
    def name_not_null(cls, value):
        if value == '':
            raise ValueError('Название не может быть пустым!')
        return value

    @validator('description', pre=True)
    def description_not_null(cls, value):
        if value == '':
            raise ValueError('Описание не может быть пустым!')
        return value

    """
    @validator('invested_amount', pre=True)
    def invested_amount_more_full_amount(cls, v, values):
        print(v)
        if 'full_amount' in values and values['full_amount'] is not None:
            print(f"full_amount {values['full_amount']}")
            if v > values['full_amount']:
                raise ValueError('!!!')
            #print(f'values = {v} values = {values}')
        # print(f'values = {values} v = {v}')
        return v
    """


class CharityProjectResponse(CharityprojectBase):
    id: int
    name: Optional[str]
    description: Optional[str]
    full_amount: Optional[int] = Field(None)
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime] = Field(None)

    class Config:
        orm_mode = True


class CharityprojectUpdateThreeFields(BaseModel):
    invested_amount: int = Field(1)
    fully_invested: bool = Field(1)
    close_date: datetime = Field(datetime.now().isoformat(timespec='seconds'))


class CharityprojectCreate(CharityprojectBase):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: Optional[PositiveInt] = Field(...)
