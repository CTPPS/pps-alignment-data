import FWCore.ParameterSet.Config as cms

ppsAlignmentConfigESSource = cms.ESSource("PPSAlignmentConfigESSource",
	label = cms.string("reference"),

	sector_45 = cms.PSet(
		rp_N = cms.PSet(
			name = cms.string("L_1_N"),
			id = cms.int32(2),

			y_cen_add = cms.double(0.),
			y_width_mult = cms.double(1.1),

			x_slice_min = cms.double(2.),
			x_slice_max = cms.double(14.)
		),
		rp_F = cms.PSet(
			name = cms.string("L_1_F"),
			id = cms.int32(3),

			y_cen_add = cms.double(0.),
			y_width_mult = cms.double(1.1),

			x_slice_min = cms.double(2.),
			x_slice_max = cms.double(14.)
		),

		cut_h_c = cms.double(0.),
		cut_v_a = cms.double(-1.13),
		cut_v_c = cms.double(-0.48),
	),

	sector_56 = cms.PSet(
		rp_N = cms.PSet(
			name = cms.string("R_1_N"),
			id = cms.int32(102),

			y_cen_add = cms.double(0.),
			y_width_mult = cms.double(1.0),

			x_slice_min = cms.double(7.),
			x_slice_max = cms.double(19.)
		),
		rp_F = cms.PSet(
			name = cms.string("R_1_F"),
			id = cms.int32(103),

			y_cen_add = cms.double(0.),
			y_width_mult = cms.double(1.0),

			x_slice_min = cms.double(7.),
			x_slice_max = cms.double(19.)
		),

		cut_h_apply = cms.bool(False),
		cut_h_c = cms.double(0.),
		cut_v_apply = cms.bool(False),
		cut_v_a = cms.double(-1.07),
		cut_v_c = cms.double(0.)
	),

	chiSqThreshold = cms.double(1000.),
	y_mode_unc_max_valid = cms.double(1.),
	y_mode_max_valid = cms.double(1.),

	matching = cms.PSet(
		reference_dataset = cms.string('../../../alig-version-2/fill_5332/xangle_140_beta_0_40/distributions.root')
	),

	x_alignment_meth_o = cms.PSet(
		rp_L_F = cms.PSet(
			x_min = cms.double(5.),
			x_max = cms.double(15.)
		),
		rp_L_N = cms.PSet(
			x_min = cms.double(6.),
			x_max = cms.double(15.)
		)
	),

	binning = cms.PSet(
		pixel_x_offset = cms.double(0.)
	)
)