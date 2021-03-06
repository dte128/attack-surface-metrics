package com.example.kevin.helloandroid;

import android.content.Intent;
import android.content.IntentSender;
import android.net.Uri;
import android.os.Parcel;
import android.support.annotation.NonNull;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.CheckBox;
import android.widget.TextView;

import java.util.List;


public class MainActivity extends ActionBarActivity {

    Greeter myGreeter;

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        this.myGreeter = new Greeter("Kevin");
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    public void button_call_data_presenter_onClick(View button)
    {
        Intent intent = new Intent(this, DataPresenterActivity.class);
        startActivity(intent);

        Intent[] il = null;
        IntentSender is = null;

        android.content.ContentResolver cr = getContentResolver();

        Uri uri = null;

        cr.insert(uri, null);



        setContentView(0);
        startActivities(il);
        startActivityForResult(intent, 0);
        startActivityFromChild(new DataPresenterActivity(), intent, 0);
        startActivityIfNeeded(intent, 0);
        try
        {
            startIntentSender(is, intent, 0, 0, 0);
        }
        catch (Exception ex) { }

        try
        {
            startIntentSenderForResult(is, 0, intent, 0, 0, 0);
        }
        catch (Exception ex) { }

        try
        {
            startIntentSenderFromChild(new DataPresenterActivity(), is, 0, intent, 0, 0, 0);
        }
        catch (Exception ex) { }
    }

    public void button_salute_onClick(View button)
    {
        String salutation = myGreeter.sayHello();

        TextView tv = (TextView)this.findViewById(R.id.textView_Greeting);
        tv.setText(salutation);

        CheckBox cb = (CheckBox)this.findViewById(R.id.checkBox_test);
        cb.setChecked(true);
    }

    public void button_saluteWorld_onClick(View button)
    {
        myGreeter.setName("Mundo");
        String salutation = myGreeter.sayHelloInSpanish();

        TextView tv = (TextView)this.findViewById(R.id.textView_Greeting);
        tv.setText(salutation);
    }
}