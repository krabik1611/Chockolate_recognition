package team.au.aucollect;


import android.net.Uri;
import android.os.StrictMode;
import android.util.Log;
import org.json.JSONException;

import java.io.*;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketAddress;
import java.net.UnknownHostException;

public class Client  {
    private Socket socket;
    private static final String adr = "10.11.4.12";
    private static final int port = 4004;
    private static final int timeout = 2000;
    private int bytesRead;

    public Client(){
        socket = new Socket();
        Log.i("Connect","Object create");


    };

    public boolean createConnection(){
        try {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder()
                    .permitAll().build();

            StrictMode.setThreadPolicy(policy);
            Log.i("Connect","Start Connected");
            SocketAddress socketAddress = new InetSocketAddress("10.11.4.12", 4004);
            socket.connect(socketAddress,timeout);
            Log.i("Connect","Connected");
            return true;
        }catch (IOException e){
            Log.i("Connect","Not Connected");
            return false;
        }

    }
    public boolean close(){
        try {
            socket.close();
            return true;
        } catch (IOException e) {
            Log.i("Connect","Not Closed");
            return false;
        }
    }

    public void send (Uri uri) throws IOException {

        String filepath = uri.getPath();
        File file = new File(filepath);
        Log.i("Connect", String.valueOf((int)file.length()));
        FileInputStream fis = new FileInputStream(file);
        FileOutputStream fos = null;
        BufferedOutputStream bos = null;
        try {
            fos = new FileOutputStream(filepath);
            bos = new BufferedOutputStream(fos);
            byte[] aByte = new byte[1024];
            int bytesRead;
            while((bytesRead = fis.read(aByte)) !=- 1){
                bos.write(aByte,0,bytesRead);
            }
            bos.flush();
            bos.close();
        } catch (IOException e) {
            Log.i("Connected",e.getMessage());
        }


    }
}
