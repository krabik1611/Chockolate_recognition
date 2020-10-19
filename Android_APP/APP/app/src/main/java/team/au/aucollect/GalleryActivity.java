package team.au.aucollect;


import androidx.appcompat.app.AppCompatActivity;

import android.net.Uri;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.widget.ImageView;

public class GalleryActivity extends AppCompatActivity {
    private static final int REQUEST_SELECT_PICTURE_FOR_FRAGMENT = 0x02;
    private final int RESULT_OK = 96;
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
    }



}