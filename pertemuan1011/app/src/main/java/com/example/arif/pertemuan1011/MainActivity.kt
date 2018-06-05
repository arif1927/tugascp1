package com.example.arif.pertemuan1011

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*
import java.util.*
import kotlin.collections.ArrayList

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val c : Calendar = Calendar.getInstance()
        val year : Int = c.get(Calendar.YEAR)
        val month : Int = c.get(Calendar.MONTH)
        val day : Int = c.get(Calendar.DAY_OF_MONTH)

        //**Menampilkan Tanggal (dd/mm/yyyy/)**//
        date.text = "$day/$month/$year"

        fun readData(): MutableList<ArrayModel>()
        val list = ArrayList<ArrayModel>()
        val text : String = etLokasi.text.toString()
        list.add(ArrayModel(rowId: 1, Lokasi: "Sutos", longitude:"-7.29462598071", latitude: "112.730369029"))
        list.add(ArrayModel(rowId: 2, Lokasi: "Narotama", longitude: "-7.288075", latitude: " 112.776449"))
        for (n: ArrayModel in list){
            if (teks==n.lokasi){
                longitude.setText(n.long)
                latitude.setText(n.lat)
                Toast.makeText( context: )
            }
        }
    }


}

class ArrayModel {

}
