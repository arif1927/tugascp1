import mapnik

m = mapnik.Map(1280,720)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()

polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('white')
r.symbols.append(polygon_symbolizer)

s.rules.append(r)
m.append_style('arif1',s)
ds = mapnik.Shapefile(file="propinsi/INDONESIA_PROP.shp")
layer = mapnik.Layer('indonesia')
layer.datasource = ds
layer.styles.append('arif1')
m.layers.append(layer)

#test

s = mapnik.Style()
r = mapnik.Rule()
basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[nama]'), 'DejaVu Sans Bold',3,mapnik.Color('red'))
basinsLabels.halo_fill = mapnik.Color('yellow')
basinsLabels.halo_radius = 1
r.symbols.append(basinsLabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
point_sym.opacity = 0.5
point_sym.file = ()
r.symbols.append(point_sym)

point = mapnik.PointSymbolizer()
r.symbols.append(point)
s.rules.append(r)

m.append_style('arif2',s)
POSTGIS_TABLE = dict(
	host='localhost',
	port='5432',
	user='postgres',
	password='pakisgunung',
	dbname='kelasgisa',

	table='(select ST_Buffer(ST_Centroid(geom),1) as geom, nama from kelasgisa) as kelasgisa'
)
ds = mapnik.PostGIS(**POSTGIS_TABLE)
layer = mapnik.Layer('arif2')
layer.datasource = ds 
layer.styles.append('arif2')
m.layers.append(layer)

m.zoom_all()
mapnik.render_to_file(m,'indonesia.jpeg','jpeg')
print "rendered image to 'indonesia.jpeg"