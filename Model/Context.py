import mysql.connector

import mysql.connector

class Context:
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pancho2004",
            database="contacts"
        )
        self.mycursor = self.mydb.cursor()
        self.create_phone_number_column()  # Agregar la llamada al método para crear el campo phone_number
        print("Info Base Datos: Conexion abierta".center(40, "*"))

    def create_phone_number_column(self):
        query = "ALTER TABLE contact ADD COLUMN phone_number VARCHAR(20)"
        try:
            self.mycursor.execute(query)
            self.mydb.commit()
            print("Campo 'phone_number' agregado a la tabla 'contact'.")
        except mysql.connector.Error as err:
            if err.errno == 1060:
                print("El campo 'phone_number' ya existe en la tabla 'contact'.")
            else:
                print("Error al agregar el campo 'phone_number':", err)
                
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.mycursor.close()
        self.mydb.close()
        print(" Info Base Datos: Conexion cerrada ".center(40, "*"))


if __name__ == "__main__":
    with Context() as context:
        print(context)