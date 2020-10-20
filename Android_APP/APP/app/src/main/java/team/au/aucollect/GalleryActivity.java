package team.au.aucollect;


import android.util.Log;
import androidx.appcompat.app.AppCompatActivity;

import android.net.Uri;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.widget.ImageView;

import java.io.IOException;
import java.net.Socket;

public class GalleryActivity extends AppCompatActivity {
    private static final int REQUEST_SELECT_PICTURE_FOR_FRAGMENT = 0x02;
    private final int RESULT_OK = 96;
    private static final String TAG = "myLogs";
    private static Client client = new Client();

    DisplayMetrics displayMetrics = new DisplayMetrics();
    ImageView imageView;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_galery);
        Init();

    }


    private void Init() {
        imageView = findViewById(R.id.imageView);
        Uri uri = (Uri) getIntent().getParcelableExtra("imageToGallery");
        imageView.setImageURI(uri);

        if (!client.createConnection()) {
            Log.i("Connection","Connect not create");
            try {
                client.send(uri);
            } catch (IOException e) {
                Log.i("Connection",e.getMessage());
            }
        }
        else Log.i("Connection","Connect create");

        if (!client.close())Log.i("Connection","Connect not close");
        else Log.i("Connection","Connect is close");
    }



}