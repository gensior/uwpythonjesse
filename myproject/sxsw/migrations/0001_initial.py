# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Party'
        db.create_table('sxsw_party', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('starttime', self.gf('django.db.models.fields.DateTimeField')()),
            ('endtime', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('drinks', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('food', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('sxsw', ['Party'])


    def backwards(self, orm):
        
        # Deleting model 'Party'
        db.delete_table('sxsw_party')


    models = {
        'sxsw.party': {
            'Meta': {'ordering': "['starttime']", 'object_name': 'Party'},
            'drinks': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'endtime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'food': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'starttime': ('django.db.models.fields.DateTimeField', [], {}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['sxsw']
