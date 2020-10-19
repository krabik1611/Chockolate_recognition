package team.au.aucollect;
import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.pm.ActivityInfo;
import android.content.pm.PackageManager;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.net.Uri;
import android.os.Bundle;
import android.os.StrictMode;
import android.util.DisplayMetrics;
import android.util.Log;
import android.util.Rational;
import android.util.Size;
import android.view.TextureView;
import android.view.View;
import android.view.ViewGroup;
import android.view.WindowManager;
import android.widget.CompoundButton;
import android.widget.ImageView;
import android.widget.Switch;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.camera.core.CameraX;
import androidx.camera.core.FlashMode;
import androidx.camera.core.ImageCapture;
import androidx.camera.core.ImageCaptureConfig;
import androidx.camera.core.Preview;
import androidx.camera.core.PreviewConfig;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.constraintlayout.widget.ConstraintSet;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import com.google.android.material.floatingactionbutton.FloatingActionButton;

import java.io.File;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketAddress;

public class CameraActivity extends AppCompatActivity {
    private static final int REQUEST_CODE_PERMISSIONS = 100;
    private static String[] REQUEST_PERMISSIONS = new String[]{
            "android.permission.CAMERA",
            "android.permission.WRITE_EXTERNAL_STORAGE",
            "android.permission.READ_EXTERNAL_STORAGE",
            "android.permission.FLASHLIGHT",
            "android.permission.INTERNET"
    };
    public static File file;
    public static ImageView frame;
    public static ViewGroup.LayoutParams params, paramsFrame, paramsTB;
    private Toolbar tbTop, tbBottom;
    private SensorManager sensorManager;
    private Sensor sensorAccel;
    private ViewGroup flashlightMenu;
    private FloatingActionButton fabFlashlight;
    private TextureView textureView;
    private DisplayMetrics dm = new DisplayMetrics();
    private Switch netStat;
    private ImageCapture imageCapture;
    private ConstraintLayout constraintLayout;
    private ConstraintSet constraintSet;
    private float[] valuesAccel = new float[3];
    private int degrees = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_camera);
        sensorManager = (SensorManager) getSystemService(SENSOR_SERVICE);
        sensorAccel = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        this.getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
        getSupportActionBar().hide();
        Init();
    }

    @Override
    protected void onResume() {
        super.onResume();
        sensorManager.registerListener(listener, sensorAccel, SensorManager.SENSOR_DELAY_NORMAL);
    }

    @Override
    protected void onPause() {
        super.onPause();
        sensorManager.unregisterListener(listener);
    }

    SensorEventListener listener = new SensorEventListener() {

        @Override
        public void onAccuracyChanged(Sensor sensor, int accuracy) {
        }

        @Override
        public void onSensorChanged(SensorEvent event) {
            switch (event.sensor.getType()) {
                case Sensor.TYPE_ACCELEROMETER:
                    for (int i = 0; i < 3; i++) {
                        valuesAccel[i] = event.values[i];
                    }
                    if (degrees != 90 && (valuesAccel[0] >= 9f || (valuesAccel[2] <= 9f && valuesAccel[1] <= 0f && valuesAccel[0] >= 7f)))
                    {
                        degrees = 90;

                        fabFlashlight.setRotation(90f);
                        flashlightMenu.setRotation(90f);
                        constraintSet = new ConstraintSet();
                        constraintSet.clone(constraintLayout);
                        constraintSet.clear(R.id.flashlightMenu,ConstraintSet.LEFT);
                        constraintSet.clear(R.id.flashlightMenu,ConstraintSet.TOP);
                        constraintSet.connect(R.id.flashlightMenu,ConstraintSet.TOP,R.id.toolbarTop,ConstraintSet.BOTTOM);
                        constraintSet.connect(R.id.flashlightMenu,ConstraintSet.LEFT,R.id.layoutparent,ConstraintSet.LEFT,100);
                        constraintSet.applyTo(constraintLayout);

                    }
                    else if (degrees != 0 && (valuesAccel[0] <= 1f && valuesAccel[0] >= -1f && valuesAccel[1] >= 4f))
                    {
                        degrees = 0;
                        fabFlashlight.setRotation(0f);
                        flashlightMenu.setRotation(0f);
                        constraintSet = new ConstraintSet();
                        constraintSet.clone(constraintLayout);
                        constraintSet.clear(R.id.flashlightMenu,ConstraintSet.LEFT);
                        constraintSet.clear(R.id.flashlightMenu,ConstraintSet.TOP);
                        constraintSet.connect(R.id.flashlightMenu,ConstraintSet.TOP,R.id.toolbarTop,ConstraintSet.BOTTOM,20);
                        constraintSet.connect(R.id.flashlightMenu,ConstraintSet.LEFT,R.id.layoutparent,ConstraintSet.LEFT,20);
                        constraintSet.applyTo(constraintLayout);

                    }
                    else if (degrees != -90 && (valuesAccel[0] <= -9f || (valuesAccel[2] <= 9f && valuesAccel[1] <= 0f && valuesAccel[0] <= -7f)))
                    {
                        degrees = -90;
                        fabFlashlight.setRotation(-90f);
                        flashlightMenu.setRotation(-90f);
                        constraintSet = new ConstraintSet();
                        constraintSet.clone(constraintLayout);
                        constraintSet.clear(R.id.flashlightMenu,ConstraintSet.LEFT);
                        constraintSet.clear(R.id.flashlightMenu,ConstraintSet.TOP);
                        constraintSet.connect(R.id.flashlightMenu,ConstraintSet.TOP,R.id.toolbarTop,ConstraintSet.BOTTOM);
                        constraintSet.connect(R.id.flashlightMenu,ConstraintSet.LEFT,R.id.layoutparent,ConstraintSet.LEFT,100);
                        constraintSet.applyTo(constraintLayout);
                    }

                    break;
            }

        }

    };

    private void Init()
    {
        textureView = findViewById(R.id.textureView);
        params = textureView.getLayoutParams();
        getWindowManager().getDefaultDisplay().getMetrics(dm);
        params.width = dm.widthPixels;
        params.height = (dm.widthPixels*16)/9;

        tbTop = findViewById(R.id.toolbarTop);
        paramsTB = tbTop.getLayoutParams();
        paramsTB.height = (dm.heightPixels - params.height) / 2;
        tbTop.setLayoutParams(paramsTB);

        tbBottom = findViewById(R.id.toolbarBottom);
        paramsTB = tbBottom.getLayoutParams();
        paramsTB.height = (dm.heightPixels - params.height) / 2;
        tbBottom.setLayoutParams(paramsTB);

        constraintLayout = findViewById(R.id.layoutparent);
        fabFlashlight = findViewById(R.id.fabFlashlight);
        flashlightMenu = findViewById(R.id.flashlightMenu);
        netStat = findViewById(R.id.netStat);

        constraintSet = new ConstraintSet();
        constraintSet.clone(constraintLayout);
        constraintSet.connect(R.id.flashlightMenu,ConstraintSet.TOP,R.id.toolbarTop,ConstraintSet.BOTTOM,20);
        constraintSet.connect(R.id.flashlightMenu,ConstraintSet.LEFT,R.id.layoutparent,ConstraintSet.LEFT,20);
        constraintSet.applyTo(constraintLayout);


        textureView.setLayoutParams(params);
        if (PermissionGranted())
        {
            StartCamera();
        }
        else
        {
            ActivityCompat.requestPermissions(this,REQUEST_PERMISSIONS,REQUEST_CODE_PERMISSIONS);
        }
        ButtonHandler();

    }

    private void ButtonHandler()
    {
        netStat.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                if (compoundButton.isChecked())
                {
                    if (!itsOnline(getApplicationContext()))
                    {
                        compoundButton.setChecked(false);
                    }
                    else
                    {
                        netStat.setText("Online");
                    }
                }
                else
                {
                    netStat.setText("Offline");
                }
            }
        });
        findViewById(R.id.fabFlashlight).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (flashlightMenu.getVisibility() == View.GONE)
                {
                    flashlightMenu.setVisibility(View.VISIBLE);
                }
                else
                {
                    flashlightMenu.setVisibility(View.GONE);
                }
            }
        });
        findViewById(R.id.btnFlashAUTO).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                fabFlashlight.setImageResource(R.drawable.flashauto);
                imageCapture.setFlashMode(FlashMode.AUTO);
                flashlightMenu.setVisibility(View.GONE);
            }
        });
        findViewById(R.id.btnFlashOFF).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                fabFlashlight.setImageResource(R.drawable.flashoff);
                imageCapture.setFlashMode(FlashMode.OFF);
                flashlightMenu.setVisibility(View.GONE);

            }
        });
        findViewById(R.id.btnFlashON).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                fabFlashlight.setImageResource(R.drawable.flashon);
                imageCapture.setFlashMode(FlashMode.ON);
                flashlightMenu.setVisibility(View.GONE);

            }
        });
    }

    private void StartCamera()
    {
        CameraX.unbindAll();
        Rational ratio = new Rational(textureView.getWidth(),textureView.getHeight());
        Size screen = new Size(dm.widthPixels,dm.heightPixels);
        PreviewConfig previewConfig = new PreviewConfig.Builder().setTargetAspectRatio(ratio).setTargetResolution(screen).build();
        Preview preview = new Preview(previewConfig);
        preview.setOnPreviewOutputUpdateListener(
                new Preview.OnPreviewOutputUpdateListener() {
                    @Override
                    public void onUpdated(Preview.PreviewOutput output) {
                        ViewGroup parent = (ViewGroup) textureView.getParent();
                        parent.removeView(textureView);
                        parent.addView(textureView,0);
                        textureView.setSurfaceTexture(output.getSurfaceTexture());

                    }
                }
        );
        ImageCaptureConfig imageCaptureConfig = new ImageCaptureConfig.Builder().
                setCaptureMode(ImageCapture.CaptureMode.MAX_QUALITY).build();
        imageCapture = new ImageCapture(imageCaptureConfig);
        findViewById(R.id.fab).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                final File filedirs = new File(getFilesDir() + "/TranslateBraille/");
                filedirs.mkdirs();
                file = new File(filedirs, "photo.jpg");
                imageCapture.takePicture(file, new ImageCapture.OnImageSavedListener() {
                    @Override
                    public void onImageSaved(@NonNull File file) {
                        String msg = "Picture saved at " + file.getAbsolutePath();
                        Log.d("path", msg);
                        Intent intent = new Intent(getApplicationContext(), CropActivity.class);
                        intent.putExtra("imageUri", Uri.fromFile(file));
                        startActivity(intent);

                    }

                    @Override
                    public void onError(@NonNull ImageCapture.UseCaseError useCaseError, @NonNull String message, @Nullable Throwable cause) {
                        String msg = "Picture was not captured: " + message;
                        Toast.makeText(CameraActivity.this, msg, Toast.LENGTH_SHORT).show();
                        if (cause != null)
                        {
                            cause.printStackTrace();
                        }
                    }
                });
            }
        });
        CameraX.bindToLifecycle(this, preview, imageCapture);


    }



    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == REQUEST_CODE_PERMISSIONS && PermissionGranted())
        {
            StartCamera();
        }
        else
        {
            Toast.makeText(this, "Permission was denied by the user!", Toast.LENGTH_SHORT).show();
            finish();
        }
    }

    private boolean PermissionGranted() {
        for (String permission : REQUEST_PERMISSIONS)
        {
            if (ContextCompat.checkSelfPermission(this,permission) != PackageManager.PERMISSION_GRANTED)
            {
                return false;
            }
        }
        return true;
    }

    public static boolean itsOnline(Context context) {
        try {
            Log.d("COMPOUND","зашел");
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder()
                    .permitAll().build();

            StrictMode.setThreadPolicy(policy);

            int timeoutMs = 2000;
            Socket sock = new Socket();
            SocketAddress sockaddr = new InetSocketAddress("8.8.8.8", 53);

            sock.connect(sockaddr, timeoutMs);
            sock.close();
            Log.i("CONNECTION STATUS:", "connected");

            return true;
        } catch (IOException ioException) {
            Log.i("CONNECTION STATUS:", "disconnected");
            return false;
        }
    }

//    @Override
//    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
//        super.onActivityResult(requestCode, resultCode, data);
//        if (requestCode == MainActivity.START_ACTIVITY_GALLERY)
//        {
//            if (resultCode == Activity.RESULT_OK)
//            {
//                Log.d("debugOK","OK");
////                String string = data.getStringExtra("path");
////                FindSymbol findSymbol = new FindSymbol();
////                findSymbol.init(string);
////                Intent intent = new Intent(getApplicationContext(),GalleryActivity.class);
////                startActivity(intent);
////                Intent intent = new Intent(getApplicationContext(),GalleryActivity.class);
////                intent.putExtra("imageToGallery",string);
////                startActivity(intent);
//
//            }
//        }
//    }
}
