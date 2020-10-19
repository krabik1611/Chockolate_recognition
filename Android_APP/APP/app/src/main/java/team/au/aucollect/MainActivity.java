package team.au.aucollect;

import android.content.Intent;
import android.content.pm.ActivityInfo;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;



public class MainActivity extends AppCompatActivity {
    public static final int START_ACTIVITY_GALLERY = 101;
    public static final int GET_IMAGE = 102;
    private Uri chosenImageUri;
    private Button btnToCamera, btnToUpload;
    private ImageView background;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
        this.getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        background = findViewById(R.id.backgroundMain);
        ButttonHandler();


    }

    private void ButttonHandler() {
        btnToCamera = findViewById(R.id.btnToCamera);
        btnToUpload = findViewById(R.id.btnToUpload);
        btnToCamera.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(),CameraActivity.class);
                startActivity(intent);
            }
        });
        btnToUpload.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
                intent.setType("image/*");
                startActivityForResult(intent, GET_IMAGE);
            }

        });


    }
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data)
    {
        super.onActivityResult(requestCode, resultCode, data);

        if (resultCode == RESULT_OK && requestCode == GET_IMAGE)
        {
            chosenImageUri = data.getData();
            Intent intent = new Intent(getApplicationContext(),CropActivity.class);
            intent.putExtra("imageUri",chosenImageUri);
            startActivity(intent);

        }
        else if (resultCode == RESULT_OK && requestCode == START_ACTIVITY_GALLERY)
        {

//            String string = data.getStringExtra("path");
//            FindSymbol findSymbol = new FindSymbol();
//            findSymbol.init(string);
//            Uri uri = data.getStringExtra("path");
//            Intent intent = new Intent(getApplicationContext(),GalleryActivity.class);
//            intent.putExtra("imageToGallery",uri);
//            startActivity(intent);
        }
    }

}
