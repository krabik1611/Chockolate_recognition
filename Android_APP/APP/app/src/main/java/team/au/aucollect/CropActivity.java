package team.au.aucollect;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

import com.yalantis.ucrop.UCrop;

import java.io.File;

public class CropActivity extends AppCompatActivity {
    private UCrop uCrop;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_crop);
        Init();
    }

    private void Init() {
        Uri imageUri = getIntent().getParcelableExtra("imageUri");
        Uri destinationUri = Uri.fromFile(new File(getFilesDir() + "/TranslateBraille/" + "photo.jpg"));
        UCrop.Options options = new UCrop.Options();
        uCrop = UCrop.of(imageUri,destinationUri);
        options.setCompressionQuality(100);
        options.setToolbarColor(ContextCompat.getColor(this, R.color.Мусульманский_зелёный));
        options.setStatusBarColor(ContextCompat.getColor(this, R.color.Мусульманский_зелёный));
        options.setActiveControlsWidgetColor(ContextCompat.getColor(this, R.color.Мусульманский_зелёный));
        options.setFreeStyleCropEnabled(true);
        uCrop.withOptions(options);
        uCrop.start(CropActivity.this);

    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == UCrop.REQUEST_CROP)
        {
            if (resultCode==RESULT_OK)
            {
                handleUCropResult(data);
            }
            else
            {
                finish();
            }

        }
        else
        {
            finish();
        }
    }

    private void handleUCropResult(Intent data) {
        if (data == null) {
            setResultCancelled();
            return;
        }
        final Uri resultUri = UCrop.getOutput(data);
        setResultOk(resultUri);
    }
    private void setResultOk(Uri imagePath) {
        Intent intent = new Intent(getApplicationContext(),GalleryActivity.class);
        intent.putExtra("imageToGallery",imagePath);
        startActivity(intent);
        finish();


    }
    private void setResultCancelled() {
        Intent intent = new Intent(getApplicationContext(),GalleryActivity.class);
        startActivity(intent);
        finish();
    }

}