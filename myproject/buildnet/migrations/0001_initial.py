# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Station'
        db.create_table('buildnet_station', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('buildnet', ['Station'])

        # Adding model 'Part'
        db.create_table('buildnet_part', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('buildnet', ['Part'])

        # Adding model 'Installation'
        db.create_table('buildnet_installation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('part', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['buildnet.Part'])),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['buildnet.Station'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('qrcode', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('installed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('buildnet', ['Installation'])


    def backwards(self, orm):
        
        # Deleting model 'Station'
        db.delete_table('buildnet_station')

        # Deleting model 'Part'
        db.delete_table('buildnet_part')

        # Deleting model 'Installation'
        db.delete_table('buildnet_installation')


    models = {
        'buildnet.installation': {
            'Meta': {'object_name': 'Installation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'installed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'part': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['buildnet.Part']"}),
            'qrcode': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['buildnet.Station']"})
        },
        'buildnet.part': {
            'Meta': {'object_name': 'Part'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'buildnet.station': {
            'Meta': {'object_name': 'Station'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['buildnet']
