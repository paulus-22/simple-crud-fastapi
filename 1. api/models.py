from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker

url = URL.create(
    drivername="mariadb+mariadbconnector",
    username="user",
    password="",
    host="localhost",
    database="patient_db",
    port=3307,
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Patient(Base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True)
    nama_depan = Column(String)
    nama_belakang = Column(String)
    alamat = Column(String)
    no_hp = Column(String)
    tempat_lahir = Column(String)
    tanggal_lahir = Column(Date)
    no_ktp = Column(String, unique=True)
    diagnosa = Column(String)
    status_dirawat = Column(Boolean)


Base.metadata.create_all(engine)
