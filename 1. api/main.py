from fastapi import FastAPI
from models import Patient, session

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Patient App"}


@app.post("/pasien")
def create_patient(
    nama_depan: str,
    nama_belakang: str,
    alamat: str,
    no_hp: str,
    tempat_lahir: str,
    tanggal_lahir: str,
    no_ktp: str,
    diagnosa: str,
    status_dirawat: bool = True,
):
    pasien = Patient(
        nama_depan=nama_depan,
        nama_belakang=nama_belakang,
        alamat=alamat,
        no_hp=no_hp,
        tempat_lahir=tempat_lahir,
        tanggal_lahir=tanggal_lahir,
        no_ktp=no_ktp,
        diagnosa=diagnosa,
        status_dirawat=status_dirawat,
    )
    session.add(pasien)
    session.commit()

    return {"berhasil menambahkan pasien ": pasien.nama_depan}


@app.get("/pasien")
def get_patients():
    patient_query = session.query(Patient)
    return patient_query.all()


@app.get("/pasien/{id}")
def get_patient(id: int):
    patient = session.query(Patient).get(id)
    return patient


@app.put("/update/{id}")
def update_patient(id: int, status_dirawat: bool):
    patient = session.query(Patient).get(id)
    patient.status_dirawat = status_dirawat
    session.add(patient)
    session.commit()
    return {"updated status : ": patient.nama_depan}


@app.delete("/delete/{id}")
def delete_patient(id: int):
    patient = session.query(Patient).get(id)
    session.delete(patient)
    session.commit()
    return {"deleted patient : ": patient.nama_depan}
