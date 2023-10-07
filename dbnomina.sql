-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-10-2023 a las 16:52:02
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dbnomina`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `creditos`
--

CREATE TABLE `creditos` (
  `IDCredito` int(11) NOT NULL,
  `IDEmpleado` int(11) DEFAULT NULL,
  `FechaOtorgamiento` date DEFAULT NULL,
  `MontoCredito` decimal(10,2) DEFAULT NULL,
  `TasaInteres` decimal(5,2) DEFAULT NULL,
  `PlazoCredito` int(11) DEFAULT NULL,
  `CuotasMensuales` decimal(10,2) DEFAULT NULL,
  `EstadoCredito` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `deducciones`
--

CREATE TABLE `deducciones` (
  `IDDeduccion` int(11) NOT NULL,
  `IDEmpleado` int(11) DEFAULT NULL,
  `TipoDeduccion` varchar(255) DEFAULT NULL,
  `MontoDeduccion` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `descuentos`
--

CREATE TABLE `descuentos` (
  `IDDescuento` int(11) NOT NULL,
  `IDEmpleado` int(11) DEFAULT NULL,
  `FechaAplicacionDescuento` date DEFAULT NULL,
  `TipoDescuento` varchar(255) DEFAULT NULL,
  `MontoDescuento` decimal(10,2) DEFAULT NULL,
  `DescripcionDescuento` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `IDEmpleado` int(11) NOT NULL,
  `Nombre` varchar(255) DEFAULT NULL,
  `Apellido` varchar(255) DEFAULT NULL,
  `FechaNacimiento` date DEFAULT NULL,
  `Direccion` varchar(255) DEFAULT NULL,
  `NumeroTelefono` varchar(15) DEFAULT NULL,
  `CorreoElectronico` varchar(255) DEFAULT NULL,
  `Departamento` varchar(255) DEFAULT NULL,
  `FechaContratacion` date DEFAULT NULL,
  `SalarioBase` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historialpagos`
--

CREATE TABLE `historialpagos` (
  `IDRegistro` int(11) NOT NULL,
  `IDEmpleado` int(11) DEFAULT NULL,
  `FechaPago` date DEFAULT NULL,
  `TipoPago` varchar(255) DEFAULT NULL,
  `MontoPago` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horasextras`
--

CREATE TABLE `horasextras` (
  `IDRegistroHorasExtras` int(11) NOT NULL,
  `IDEmpleado` int(11) DEFAULT NULL,
  `FechaRegistro` date DEFAULT NULL,
  `HoraInicioHorasExtras` time DEFAULT NULL,
  `HoraFinHorasExtras` time DEFAULT NULL,
  `TotalHorasExtras` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagos`
--

CREATE TABLE `pagos` (
  `IDPago` int(11) NOT NULL,
  `IDEmpleado` int(11) DEFAULT NULL,
  `FechaPago` date DEFAULT NULL,
  `TipoPago` varchar(255) DEFAULT NULL,
  `MontoPago` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registrohorastrabajadas`
--

CREATE TABLE `registrohorastrabajadas` (
  `IDRegistro` int(11) NOT NULL,
  `IDEmpleado` int(11) DEFAULT NULL,
  `FechaRegistro` date DEFAULT NULL,
  `HoraEntrada` time DEFAULT NULL,
  `HoraSalida` time DEFAULT NULL,
  `TotalHorasTrabajadas` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vacacionestiempolibre`
--

CREATE TABLE `vacacionestiempolibre` (
  `IDSolicitud` int(11) NOT NULL,
  `IDEmpleado` int(11) DEFAULT NULL,
  `TipoSolicitud` varchar(255) DEFAULT NULL,
  `FechaSolicitud` date DEFAULT NULL,
  `FechaInicio` date DEFAULT NULL,
  `FechaTermino` date DEFAULT NULL,
  `EstadoSolicitud` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `creditos`
--
ALTER TABLE `creditos`
  ADD PRIMARY KEY (`IDCredito`),
  ADD KEY `IDEmpleado` (`IDEmpleado`);

--
-- Indices de la tabla `deducciones`
--
ALTER TABLE `deducciones`
  ADD PRIMARY KEY (`IDDeduccion`),
  ADD KEY `IDEmpleado` (`IDEmpleado`);

--
-- Indices de la tabla `descuentos`
--
ALTER TABLE `descuentos`
  ADD PRIMARY KEY (`IDDescuento`),
  ADD KEY `IDEmpleado` (`IDEmpleado`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`IDEmpleado`);

--
-- Indices de la tabla `historialpagos`
--
ALTER TABLE `historialpagos`
  ADD PRIMARY KEY (`IDRegistro`),
  ADD KEY `IDEmpleado` (`IDEmpleado`);

--
-- Indices de la tabla `horasextras`
--
ALTER TABLE `horasextras`
  ADD PRIMARY KEY (`IDRegistroHorasExtras`),
  ADD KEY `IDEmpleado` (`IDEmpleado`);

--
-- Indices de la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD PRIMARY KEY (`IDPago`),
  ADD KEY `IDEmpleado` (`IDEmpleado`);

--
-- Indices de la tabla `registrohorastrabajadas`
--
ALTER TABLE `registrohorastrabajadas`
  ADD PRIMARY KEY (`IDRegistro`),
  ADD KEY `IDEmpleado` (`IDEmpleado`);

--
-- Indices de la tabla `vacacionestiempolibre`
--
ALTER TABLE `vacacionestiempolibre`
  ADD PRIMARY KEY (`IDSolicitud`),
  ADD KEY `IDEmpleado` (`IDEmpleado`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `creditos`
--
ALTER TABLE `creditos`
  MODIFY `IDCredito` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `deducciones`
--
ALTER TABLE `deducciones`
  MODIFY `IDDeduccion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `descuentos`
--
ALTER TABLE `descuentos`
  MODIFY `IDDescuento` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `IDEmpleado` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `historialpagos`
--
ALTER TABLE `historialpagos`
  MODIFY `IDRegistro` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `horasextras`
--
ALTER TABLE `horasextras`
  MODIFY `IDRegistroHorasExtras` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pagos`
--
ALTER TABLE `pagos`
  MODIFY `IDPago` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `registrohorastrabajadas`
--
ALTER TABLE `registrohorastrabajadas`
  MODIFY `IDRegistro` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `vacacionestiempolibre`
--
ALTER TABLE `vacacionestiempolibre`
  MODIFY `IDSolicitud` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `creditos`
--
ALTER TABLE `creditos`
  ADD CONSTRAINT `creditos_ibfk_1` FOREIGN KEY (`IDEmpleado`) REFERENCES `empleados` (`IDEmpleado`);

--
-- Filtros para la tabla `deducciones`
--
ALTER TABLE `deducciones`
  ADD CONSTRAINT `deducciones_ibfk_1` FOREIGN KEY (`IDEmpleado`) REFERENCES `empleados` (`IDEmpleado`);

--
-- Filtros para la tabla `descuentos`
--
ALTER TABLE `descuentos`
  ADD CONSTRAINT `descuentos_ibfk_1` FOREIGN KEY (`IDEmpleado`) REFERENCES `empleados` (`IDEmpleado`);

--
-- Filtros para la tabla `historialpagos`
--
ALTER TABLE `historialpagos`
  ADD CONSTRAINT `historialpagos_ibfk_1` FOREIGN KEY (`IDEmpleado`) REFERENCES `empleados` (`IDEmpleado`);

--
-- Filtros para la tabla `horasextras`
--
ALTER TABLE `horasextras`
  ADD CONSTRAINT `horasextras_ibfk_1` FOREIGN KEY (`IDEmpleado`) REFERENCES `empleados` (`IDEmpleado`);

--
-- Filtros para la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD CONSTRAINT `pagos_ibfk_1` FOREIGN KEY (`IDEmpleado`) REFERENCES `empleados` (`IDEmpleado`);

--
-- Filtros para la tabla `registrohorastrabajadas`
--
ALTER TABLE `registrohorastrabajadas`
  ADD CONSTRAINT `registrohorastrabajadas_ibfk_1` FOREIGN KEY (`IDEmpleado`) REFERENCES `empleados` (`IDEmpleado`);

--
-- Filtros para la tabla `vacacionestiempolibre`
--
ALTER TABLE `vacacionestiempolibre`
  ADD CONSTRAINT `vacacionestiempolibre_ibfk_1` FOREIGN KEY (`IDEmpleado`) REFERENCES `empleados` (`IDEmpleado`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
