package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;

import com.danielme.android.navigationdrawer.R;

public class CatalogActivity extends AppCompatActivity {
    private Context context=this;
    private Button detailButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.catalog_activity);
        detailButton = findViewById(R.id.detailButton);
        detailButton.setOnClickListener(view -> {
            Intent intent = new Intent(context, DetailActivity.class);
            context.startActivity(intent);
        });


    }
}