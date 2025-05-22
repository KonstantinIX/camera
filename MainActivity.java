package zxc.zxc;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends AppCompatActivity {
    private WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        webView = findViewById(R.id.webview);
        WebSettings webSettings = webView.getSettings();
        webSettings.setJavaScriptEnabled(true);          // Включить JS, если нужно
        webView.setWebViewClient(new WebViewClient());   // Открывать внутри приложения

        webView.loadUrl("http://192.168.1.13:5000/");
    }
}