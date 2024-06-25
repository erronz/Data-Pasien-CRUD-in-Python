pasien = [{"NIK":"3578240912950001","Nama":"Erron Hudyono","Jenis Kelamin":"Pria","Tanggal Lahir":"1995-12-09","Nomor Kontak":"087853678991","Alamat":"Kedungdoro raya X/15"},
{"NIK":"2105042102980001","Nama":"Azalia Arinal","Jenis Kelamin":"Wanita","Tanggal Lahir":"1998-02-21","Nomor Kontak":"089843859201","Alamat":"Puri Raya Blok A/5"},
{"NIK":"3578241901960001","Nama":"M. Fairuzzuddin","Jenis Kelamin":"Pria","Tanggal Lahir":"1996-01-19","Nomor Kontak":"081844102201","Alamat":"Sepanjang Timur I/3"},
{"NIK":"1871131011980001","Nama":"Dinda Nuswantara","Jenis Kelamin":"Wanita","Tanggal Lahir":"1998-11-10","Nomor Kontak":"081871169200","Alamat":"Kaliasin Timur II/21"},
{"NIK":"3578242803930001","Nama":"Nindia Putri","Jenis Kelamin":"Wanita","Tanggal Lahir":"1993-03-28","Nomor Kontak":"084876169292","Alamat":"Villa Bukit Mas Selatan IIIA/21"}]

list = {}
def konfirmasi():
    print("1. Lanjutkan")
    print("2. Batalkan")
    v_confirm=input("Masukkan angka Menu yang ingin dijalankan: ")
    return v_confirm
def ubah_data_pasien():
    data_pasien()
    v_pos = data_pasien_nik()   
    if v_pos == 100: #tidak ada datanya
        return
    v_pos = int(v_pos)-10
    temp_pasien=pasien[v_pos].copy()
    while True:  
        print()
        print("1. Perbaharui Nama")
        print("2. Perbaharui Jenis Kelamin")
        print("3. Perbaharui Tanggal Lahir")
        print("4. Perbaharui Nomor Kontak")
        print("5. Perbaharui Alamat")
        print("6. Kembali ke Menu Data Pasien") 
        print("99. Simpan Perubahan")
        
        v_udp = input("Masukkan angka Menu yang ingin dijalankan: ")
        if not v_udp.isdigit():
            not_digit()
        else:            
            if int(v_udp) == 1:
                nama_baru = tambah_data_pasien_nama()
                temp_pasien["Nama"] = nama_baru
            elif int(v_udp) == 2:
                gender_baru = tambah_data_pasien_gender()
                temp_pasien["Jenis Kelamin"] = gender_baru
            elif int(v_udp) == 3: 
                ttl_baru = tambah_data_pasien_birthdate()
                temp_pasien["Tanggal Lahir"] = ttl_baru
            elif int(v_udp) == 4:
                nomor_baru = tambah_data_pasien_nomor()
                temp_pasien["Nomor Kontak"] = nomor_baru
            elif int(v_udp) == 5:
                alamat_baru = tambah_data_pasien_alamat()
                temp_pasien["Alamat"] = alamat_baru
            elif int(v_udp) == 99:
                del pasien[v_pos]
                pasien.append(temp_pasien) 
                return
            elif int(v_udp) == 6:
                return
            else:
                print(f"Angka menu tidak valid. Silahkan dicoba lagi!")
            print(f"\n\t\t\t\t--Daftar Data Pasien--")
            print(f"Index\tNIK Pasien\t\tNama Pasien\t\tJenis Kelamin\tTanggal Lahir\tNomor Kontak\tAlamat")
            print(1,end= "\t")
            for column in temp_pasien:
                if column == "Nama":
                    print(temp_pasien[column].ljust(18), end= "\t")
                elif column == "Jenis Kelamin":
                    print(temp_pasien[column], end= "\t\t")
                else:
                    print(temp_pasien[column], end= "\t")

def hapus_data_pasien():
    data_pasien()
    while True:
        v_nik = input("Masukkan NIK Pasien Untuk Dihapus: ")
        if not v_nik.isdigit():
            not_digit()
        else:
            len_p = len(pasien)
            count_p = 0
            for i in range(len_p):
                if pasien[i]["NIK"] != v_nik:
                    count_p+=1    
                elif pasien[i]["NIK"] == v_nik:
                    print(f"Data Pasien dengan NIK {v_nik} akan dihapus!")
                    v_confirm=konfirmasi()
                    if not v_confirm.isdigit():
                        not_digit()
                    elif int(v_confirm)==1:
                        del pasien[i]
                        print(f"Data Pasien dengan NIK {v_nik} berhasil dihapus!")
                        return
                    elif int(v_confirm)==2:
                        print(f"Penghapusan data pasien dibatalkan!")
                        return
                    else:
                        print(f"Angka menu tidak valid. Silahkan dicoba lagi!")
                if count_p == len_p:
                    print(f"Data Pasien dengan NIK {v_nik} tidak ditemukan!")
                    return  
def tambah_data_pasien():
    while True:
        v_nik = input("Masukkan NIK Pasien Untuk Ditambahkan: ")
        if not v_nik.isdigit():
            not_digit()
        elif len(v_nik) != 16:
            print("NIK wajib 16 digit!")
        else:
            len_p = len(pasien)
            countx = 0
            for i in range(len_p):
                if pasien[i]["NIK"] != v_nik:
                    countx+=1
                    continue
            if countx != len_p:
                print(f"NIK {v_nik} sudah pernah terdaftar!")
            elif countx == len_p:  
                     
                list["NIK"]= v_nik
                tambah_data_pasien_nama()
                tambah_data_pasien_gender()
                tambah_data_pasien_birthdate()      
                tambah_data_pasien_nomor()   
                tambah_data_pasien_alamat()                
                print(f"Index\tNIK Pasien\t\tNama Pasien\t\tJenis Kelamin\tTanggal Lahir\tNomor Kontak\tAlamat")
                print(1,end= "\t")
                for i,j in list.items():
                    if i == "Nama":
                        print(j.ljust(18), end= "\t")
                    elif i == "Jenis Kelamin":
                        print(j, end= "\t\t")
                    else:
                        print(j, end= "\t")
                print()                        
                while True:
                    v_confirm = konfirmasi()
                    if not v_confirm.isdigit():
                        not_digit()
                    elif int(v_confirm)==1:
                        pasien.append(list)
                        print(f"\t\t\t\t--Data Pasien Berhasil Ditambahkan!--")
                        return
                    elif int(v_confirm)==2:
                        print(f"Penambahan data pasien dibatalkan!")
                        return
                    else:
                        print(f"Angka menu tidak valid. Silahkan dicoba lagi!")
                    continue
                    
    
def tambah_data_pasien_nama():
    while True:
        v_nama = input("Masukkan Nama: ")
        len_nama = len(v_nama)
        count_p = 0
        for char in v_nama:
            if char.isdigit(): 
                print("Nama tidak diperbolehkan mengandung angka!\n")
                break
            else:
                count_p+=1
            if count_p == len_nama:
                list["Nama"]= v_nama
                return v_nama
                
    return
def tambah_data_pasien_gender():
    while True:
        v_gender = input("1. Pria\n2. Wanita\nPilih Jenis Kelamin: ")
        if not v_gender.isdigit():
            not_digit()
        elif int(v_gender)==1:
            list["Jenis Kelamin"]="Pria"
            return "Pria"
        elif int(v_gender)==2:
            list["Jenis Kelamin"]="Wanita"    
            return "Wanita" 
        else:
            print(f"Angka Menu tidak valid!") 

def tambah_data_pasien_birthdate():
    while True:
        v_bd = input("Masukkan Tanggal Lahir (format: yyyymmdd, contoh: 20241231): ")
        len_bd = len(v_bd)
        len_char = 0
        for char in v_bd:
            len_char+=1
            if not char.isdigit(): 
                print("Tanggal hanya boleh mengandung angka!\n")
                break
            else:
                if len_bd == 8:
                    if int(v_bd[4:6])>12:
                        print(f"Bulan {v_bd[4:6]} tidak valid!\n")
                        break
                    elif int(v_bd[-2:])>31 and int(v_bd[4:6]) in [1,3,5,7,8,10,12]:
                        print(f"Tanggal {v_bd[-2:]} tidak terdapat pada Bulan {v_bd[4:6]}!\n")
                        break
                    elif int(v_bd[-2:])>30 and int(v_bd[4:6]) in [4,6,9,11]:
                        print(f"Tanggal {v_bd[-2:]} tidak terdapat pada Bulan {v_bd[4:6]}!\n")
                        break
                    elif int(v_bd[-2:])>28 and int(v_bd[4:6])==2 and int(v_bd[:4])%4!=0:
                        print(f"Tanggal {v_bd[-2:]} tidak terdapat pada Bulan {v_bd[4:6]}!\n")
                        break
                    elif int(v_bd[-2:])>29 and int(v_bd[4:6])==2 and int(v_bd[:4])%4==0:
                        print(f"Tanggal {v_bd[-2:]} tidak terdapat pada Bulan {v_bd[4:6]}!\n")
                        break
                    elif len_char == len_bd:
                        list["Tanggal Lahir"]= v_bd[:4]+"-"+v_bd[4:6]+"-"+v_bd[-2:]
                        return v_bd[:4]+"-"+v_bd[4:6]+"-"+v_bd[-2:]
                else: 
                    print("Format Tanggal Lahir harus dalam 8 digit! (yyyymmdd)\n")
                    break

def tambah_data_pasien_nomor():
    while True:
        v_hp = input("Masukkan Nomor Kontak: ")
        len_hp = len(v_hp)
        len_char = 0
        for char in v_hp:
            len_char+=1
            if not char.isdigit(): 
                print("Nomor Kontak hanya boleh mengandung angka!\n")
                break
            else:
                if len_hp > 13: 
                    print("Nomor Kontak maksimal 13 digit!\n")
                    break                    
                elif len_char == len_hp:
                    list["Nomor Kontak"]= v_hp
                    return v_hp
            
def tambah_data_pasien_alamat():
    while True:
        v_alamat = input("Masukkan Alamat: ")
        len_alamat = int(len(v_alamat))
        if len_alamat > 25:
            print("Alamat maksimal 40 karakter!\n")
            continue
        else :
            list["Alamat"]= v_alamat
            return v_alamat

def data_pasien_spesifik():
    data_pasien()
    while True:        
        print()
        print(f"1. Mencari Dengan Data NIK")
        print(f"2. Mencari Dengan Data Nomor Kontak")
        print(f"3. Kembali ke Menu Data Pasien")
        print(f"4. Kembali ke Menu Utama")
        v_dps = input("Masukkan angka Menu yang ingin dijalankan: ")
        if not v_dps.isdigit():
            not_digit()
        else:
            v_dps = int(v_dps)
            if v_dps == 1:
                output_dps = data_pasien_nik()
                if output_dps == 1:
                    return
                elif output_dps == 2:
                    return output_dps
            elif v_dps == 2:
                output_dps = data_pasien_phone()
                if output_dps == 1:
                    return
                elif output_dps == 2:
                    return output_dps
            elif v_dps == 3:
                return
            elif v_dps == 4:
                return 4
            else:
                print(f"Angka menu tidak valid. Silahkan dicoba lagi!")

def data_pasien_nik():
    v_len = len(pasien)
    v_count = 0
    v_index = 1
    while True:
        v_input = input("Masukkan NIK yang akan diproses: ")
        if not v_input.isdigit():
            not_digit()
        else:
            for row in range(v_len):
                if pasien[row]["NIK"] == v_input:
                    print(f"\n\t\t\t\t--Daftar Data Pasien--")
                    print(f"Index\tNIK Pasien\t\tNama Pasien\t\tJenis Kelamin\tTanggal Lahir\tNomor Kontak\tAlamat")
                    print(v_index,end= "\t")
                    v_index += 1
                    for column in pasien[row]:
                        if column == "Nama":
                            print(pasien[row][column].ljust(18), end= "\t")
                        elif column == "Jenis Kelamin":
                            print(pasien[row][column], end= "\t\t")
                        else:
                            print(pasien[row][column], end= "\t")
                    print()
                    return int(row)+10
                else: v_count+= 1
                if v_count == v_len: 
                    print("Data Pasien Tidak Ditemukan")
            print()
            # output_dp = back_menu_pasien()
            return 100

def data_pasien_phone():
    v_len = len(pasien)
    v_count = 0
    v_index = 1
    while True:
        v_input = input("Masukkan Nomor Kontak: ")
        if not v_input.isdigit():
            not_digit()
        else:
            for row in range(v_len):
                if pasien[row]["Nomor Kontak"] == v_input:
                    print(f"\n\t\t\t\t--Daftar Data Pasien--")
                    print(f"Index\tNIK Pasien\t\tNama Pasien\t\tJenis Kelamin\tTanggal Lahir\tNomor Kontak\tAlamat")
                    print(v_index,end= "\t")
                    v_index += 1
                    for column in pasien[row]:
                        if column == "Nama":
                            print(pasien[row][column].ljust(18), end= "\t")
                        elif column == "Jenis Kelamin":
                            print(pasien[row][column], end= "\t\t")
                        else:
                            print(pasien[row][column], end= "\t")
                    print()
                    return
                else: v_count+= 1
                if v_count == v_len: 
                    print("Data Pasien Tidak Ditemukan")
            print()
            return

def data_pasien():
    v_len = len(pasien)
    print(f"\n\t\t\t\t--Daftar Data Pasien--")
    print(f"Index\tNIK Pasien\t\tNama Pasien\t\tJenis Kelamin\tTanggal Lahir\tNomor Kontak\tAlamat")
    for row in range(v_len):
        print(row+1,end= "\t")
        for column in pasien[row]:
            if column == "Nama":
                print(pasien[row][column].ljust(18), end= "\t")
            elif column == "Jenis Kelamin":
                print(pasien[row][column], end= "\t\t")
            elif column == "Nomor Kontak":
                print(pasien[row][column].ljust(13), end= "\t")
            else:
                print(pasien[row][column], end= "\t")
        print()      
    #output_dp = back_menu_pasien()
    return 

def back_menu_pasien():
    while True:
        v_rmp = return_menu_pasien()
        if not v_rmp.isdigit():
            not_digit()
        else:
            v_rmp = int(v_rmp)  
            if v_rmp == 1:
                return 1
            elif v_rmp == 2:
                return 2
            else:
                print(f"Angka menu tidak valid. Silahkan dicoba lagi!")

def return_menu_pasien():
    print()
    print(f"1. Kembali ke Menu Data Pasien")
    print(f"2. Kembali ke Menu Utama")
    v_menu3 = input("Masukkan angka Menu yang ingin dijalankan: ")
    return v_menu3


def not_digit():
    print(f"Error! Harap masukkan inputan data dalam angka!")

def menu_utama():
    print(f"\n\t\t--Selamat datang di Aplikasi Rekam Medis Pasien--")
    print(f"1. Data Pasien")
    print(f"2. Log Off")
    v_menu1 = input("Masukkan angka Menu yang ingin dijalankan: ")
    return v_menu1

def menu_utama_exe():
    while True:
        v_mu = menu_utama()
        if not v_mu.isdigit():
            not_digit()
        else:
            v_mu = int(v_mu)        
            if v_mu == 1:
                menu_pasien_exe()
            elif v_mu ==2:
                print("Program Shut Down!")
                break
            elif v_mu ==3:
                print("Program Shut Down!")
                break
                menu_rmedis()
            else:
                print(f"Angka menu tidak valid. Silahkan dicoba lagi!")

def menu_pasien():
    print(f"\n\t\t--Data Pasien--")
    print(f"1. Menampilkan Data Pasien Secara Keseluruhan")
    print(f"2. Menambahkan Data Pasien Baru")
    print(f"3. Memperbaharui Data Pasien")
    print(f"4. Menghapus Data Pasien")
    print(f"5. Menu Utama")
    v_menu2 = input("Masukkan angka Menu yang ingin dijalankan: ")
    return v_menu2

def menu_pasien_exe():
    while True:
        v_mp = menu_pasien()    
        if not v_mp.isdigit():
            not_digit()
        else:
            v_mp = int(v_mp)
            if v_mp == 1:
                output_dp = data_pasien_spesifik()
                if output_dp == 4:
                    return
                v_mp = "a"
            elif v_mp == 2:
                print("\nSilahkan mengisi kelengkapan data pasien baru: ")
                output_dp2 = tambah_data_pasien()
                if output_dp2 == 2:
                    return
                v_mp = "a"
            elif v_mp == 3:
                print("\nSilahkan mengisi kelengkapan data pasien yang akan diperbaharui: ")
                output_dp2 = ubah_data_pasien()
                if output_dp2 == 2:
                    return
                v_mp = "a"                
            elif v_mp == 4:
                hapus_data_pasien()
                v_mp = "a"
            elif v_mp == 5:
                return
            else:
                print(f"Angka menu tidak valid. Silahkan dicoba lagi!")



menu_utama_exe()
#tambah_data_pasien()