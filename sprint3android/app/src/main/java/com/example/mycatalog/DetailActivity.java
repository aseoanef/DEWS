package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.res.Configuration;
import android.os.Bundle;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        switch (getResources().getConfiguration().orientation) {
            case Configuration.ORIENTATION_PORTRAIT:
                setContentView(R.layout.detail_activity);
                break;
            case Configuration.ORIENTATION_LANDSCAPE:
                setContentView(R.layout.detail_land);
                break;
        }
    }
}