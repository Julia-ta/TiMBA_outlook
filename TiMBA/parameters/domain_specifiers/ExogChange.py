from TiMBA.parameters.domain_specifiers.AbstractDomainSpecifier import DomainNameSpecifier, SplitDomainSpecifier, \
    MainDomainSpecifier, SubDomainSpecifier, FinalDomainSpecifier, RegionCodeSpecifier


class ExogChangeSupply(DomainNameSpecifier, RegionCodeSpecifier, FinalDomainSpecifier, SubDomainSpecifier):
    region_code = "RegionCode"
    commodity_code = "CommodityCode"

    elasticity_price = "SPriceElast"
    growth_rate_value = "SGrowth"
    growth_rate_gdp = "SGDPGrowth"
    elasticity_gdp = "SGDPElast"
    growth_rate_fourth_shift = "SfourthGrowth"
    growth_rate_fifth_shift = "SfifthGrowth"
    growth_rate_sixth_shift = "SsixthGrowth"
    growth_rate_upper_bound = "SUBGrowth"

    header_description = {
        "Unnamed: 1": region_code,
        "Unnamed: 3": commodity_code,
        "Unnamed: 7": elasticity_price,
        "Unnamed: 8": growth_rate_value,
        "Unnamed: 9": growth_rate_gdp,
        "Unnamed: 10": growth_rate_fourth_shift,
        "Unnamed: 11": growth_rate_fifth_shift,
        "Unnamed: 12": growth_rate_sixth_shift,
        "Unnamed: 13": growth_rate_upper_bound
    }

    # Excel Start Idx
    splitting_mask = "S"
    column_index = 0
    mask_axis = 0


class ExogChangeDemand(DomainNameSpecifier, RegionCodeSpecifier, FinalDomainSpecifier, SubDomainSpecifier):
    region_code = "RegionCode"
    commodity_code = "CommodityCode"

    elasticity_price = "DPriceElast"
    growth_rate_value = "DGrowth"
    growth_rate_gdp = "GDPGrowth"
    growth_demand_expected = "ExpectedDemandGrowth"
    growth_lower_bound = "DLBGrowth"
    elasticity_gdp = "DGDPElast"

    header_description = {
        "Unnamed: 1": region_code,
        "Unnamed: 3": commodity_code,
        "Unnamed: 7": elasticity_price,
        "Unnamed: 8": growth_rate_value,
        "Unnamed: 9": growth_rate_gdp,
        "Unnamed: 10": growth_demand_expected, #TODO check correct column
        "Unnamed: 15": growth_lower_bound,
        "Unnamed: 17": elasticity_gdp
    }

    # Excel Start Idx
    splitting_mask = "D"
    column_index = 0
    mask_axis = 0


class ExogChangeForest(DomainNameSpecifier, RegionCodeSpecifier, FinalDomainSpecifier, SubDomainSpecifier):
    region_code = "RegionCode"

    growth_rate_stock = "StockChange"
    growth_rate_area = "AreaChange"
    growth_rate_gdp = "FGDPGrowth"
    adjustment_endogenous_growth_rate_stock = "AdjusEndoForSt"
    elasticity_growth_rate_stock_on_area = "StockElastArea"
    growth_rate_linear_GDP_forest_area_growth_rate = "ForAreaGDPGrowth"
    growth_rate_squared_GDP_forest_area_growth_rate = "SqForAreaGDPGrowth"
    fraction_fuelwood = "FuelwoodForest"
    ratio_inventory_drain = "InventoryDrain"
    max_ratio_inventory_drain = "MaxRatioInventoryDrain"

    header_description = {
        "Unnamed: 1": region_code,
        "Unnamed: 7": growth_rate_stock,
        "Unnamed: 8": growth_rate_area,
        "Unnamed: 9": growth_rate_gdp,
        "Unnamed: 10": adjustment_endogenous_growth_rate_stock,
        "Unnamed: 11": elasticity_growth_rate_stock_on_area,
        "Unnamed: 12": growth_rate_linear_GDP_forest_area_growth_rate,
        "Unnamed: 13": growth_rate_squared_GDP_forest_area_growth_rate,
        "Unnamed: 14": fraction_fuelwood,
        "Unnamed: 15": ratio_inventory_drain,
        "Unnamed: 16": max_ratio_inventory_drain,
    }

    # Excel Start Idx
    splitting_mask = "F"
    column_index = 0
    mask_axis = 0


class ExogChangeManufactureCost(DomainNameSpecifier, RegionCodeSpecifier, FinalDomainSpecifier, SubDomainSpecifier):
    region_code = "RegionCode"
    commodity_code = "CommodityCode"
    secondary_commodity = "Secondary_commodity"
    process_number = "process_number"
    input_mix_number = "input_mix_number"
    growth_rate_net_manufacture_cost = "ManuCostChange"

    header_description = {
        "Unnamed: 1": region_code,
        "Unnamed: 3": commodity_code,
        "Unnamed: 4": secondary_commodity,
        "Unnamed: 5": process_number,
        "Unnamed: 6": input_mix_number,
        "Unnamed: 7": growth_rate_net_manufacture_cost
    }

    # Excel Start Idx
    splitting_mask = "M"
    column_index = 0
    mask_axis = 0


class ExogChangeManufactureCoefficients(DomainNameSpecifier, RegionCodeSpecifier, FinalDomainSpecifier,
                                        SubDomainSpecifier):
    region_code = "RegionCode"
    commodity_code = "Input_commodity"
    output_commodity = "Output_commodity"
    process_number = "process_number"
    input_mix_number = "input_mix_number"
    change_input_output = "ManuCoeff"

    header_description = {
        "Unnamed: 1": region_code,
        "Unnamed: 3": commodity_code,
        "Unnamed: 4": output_commodity,
        "Unnamed: 5": process_number,
        "Unnamed: 6": input_mix_number,
        "Unnamed: 7": change_input_output
    }

    # Excel Start Idx
    splitting_mask = "P"
    column_index = 0
    mask_axis = 0


class ExogChangeTradeImport(DomainNameSpecifier, SubDomainSpecifier, FinalDomainSpecifier, RegionCodeSpecifier):
    origin_region = "Origin_region"  # Region Code of origin
    region_code = "country"

    commodity_code = "CommodityCode"
    change_freight_cost = "FreightChange"
    change_import_tax_rate = "ImpTaxChange"
    change_export_tax_rate = "ExpTaxChange"
    exogenous_growth_rate_export_trade_shift = "TradeGrowth"
    elasticity_trade_exporter_shift = "TradeElast"
    exogenous_growth_rate_import_trade_shift = "TradeGrowthImp"
    elasticity_trade_importer_shift = "TradeElast"
    trade_inertia_bounds = "TradeBounds"

    header_description = {
        "Unnamed: 1": origin_region,
        "Unnamed: 3": region_code,
        "Unnamed: 5": commodity_code,
        "Unnamed: 7": change_freight_cost,
        "Unnamed: 8": change_import_tax_rate,
        "Unnamed: 9": change_export_tax_rate,
        "Unnamed: 10": exogenous_growth_rate_export_trade_shift,
        "Unnamed: 11": elasticity_trade_exporter_shift,
        "Unnamed: 12": exogenous_growth_rate_import_trade_shift,
        "Unnamed: 13": elasticity_trade_importer_shift,
        "Unnamed: 14": trade_inertia_bounds
    }
    splitting_mask = "zz"
    column_index = 1
    mask_axis = 0


class ExogChangeTradeExport(DomainNameSpecifier, SubDomainSpecifier, FinalDomainSpecifier, RegionCodeSpecifier):
    region_code = "Origin_region"  # Region Code of origin
    destination_region_code = "country"

    commodity_code = "CommodityCode"
    change_freight_cost = "FreightChange"
    change_import_tax_rate = "ImpTaxChange"
    change_export_tax_rate = "ExpTaxChange"
    exogenous_growth_rate_export_trade_shift = "TradeGrowth"
    elasticity_trade_exporter_shift = "TradeElast"
    exogenous_growth_rate_import_trade_shift = "TradeGrowthImp"
    elasticity_trade_importer_shift = "TradeElastImp"
    trade_inertia_bounds = "TradeBounds"

    header_description = {
        "Unnamed: 1": region_code,
        "Unnamed: 3": destination_region_code,
        "Unnamed: 5": commodity_code,
        "Unnamed: 7": change_freight_cost,
        "Unnamed: 8": change_import_tax_rate,
        "Unnamed: 9": change_export_tax_rate,
        "Unnamed: 10": exogenous_growth_rate_export_trade_shift,
        "Unnamed: 11": elasticity_trade_exporter_shift,
        "Unnamed: 12": exogenous_growth_rate_import_trade_shift,
        "Unnamed: 13": elasticity_trade_importer_shift,
        "Unnamed: 14": trade_inertia_bounds
    }
    splitting_mask = "zz"
    column_index = 3
    mask_axis = 0


class ExogChangeTrade(DomainNameSpecifier, SubDomainSpecifier, SplitDomainSpecifier):

    # Excel Start Idx
    splitting_mask = "T"
    column_index = 0
    mask_axis = 0

    domain_split_list = [
        ExogChangeTradeImport(),
        ExogChangeTradeExport()
    ]


class ExogChange(DomainNameSpecifier, MainDomainSpecifier, SplitDomainSpecifier):
    # Excel Start Idx
    content_start_index = 126
    domain_split_list = [
        ExogChangeSupply(),
        ExogChangeDemand(),
        ExogChangeForest(),
        ExogChangeTrade(),
        ExogChangeManufactureCoefficients(),
        ExogChangeManufactureCost()
    ]
