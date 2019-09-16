import sqlite3


with sqlite3.connect(r'./datumproject/db.sqlite3') as conn:
    conn.enable_load_extension(True)
    conn.execute("SELECT load_extension('mod_spatialite.dll')")
    conn.execute("SELECT InitSpatialMetaData()")

    c = conn.cursor()

    c.execute("insert into DatumApp_type ( name, description ) values ( 'education', 'Education' )")
    c.execute("insert into DatumApp_type ( name, description ) values ( 'liesure', 'Liesure' )")
    c.execute("insert into DatumApp_type ( name, description ) values ( 'sport', 'Sport' )")
    c.execute("""insert into DatumApp_object (id, name, description, type_id, geo_coord) 
                 values (1, 'school' , 'school description', 1, GeomFromText('POINT(1.01 2.02)', 4326))""")
    c.execute('select * from DatumApp_object')
    conn.commit()
    print('done!\n', c.fetchall())
